from typing import Union
from fastapi.security import OAuth2PasswordBearer
from fastapi import (FastAPI,
                     HTTPException,
                     Request,
                     Response,
                     Depends,
                     status)   
from datetime import timedelta, timezone, datetime
from pydantic import BaseModel
from jose import JWTError,jwt 
from motor.motor_asyncio import AsyncIOMotorClient
import os
import subprocess
from customlogger import requests_logger
import httpx

app = FastAPI()
 
JWT_EXPIRATION_MINUTES = 15
ALGORITHM = "HS256"
# Obviously, hardcoding the password is not a good practice.
MONGO_URL = f'''mongodb://admin:dummyPassword123@{os.environ.get("MONGODB_HOST","mongodb_node") }:{os.environ.get("MONGODB_HOST_PORT",27017)}/CaseStudy3?authSource=admin'''


SECRET_KEY = os.environ.get("SECRET_KEY")


CLIENT = AsyncIOMotorClient(MONGO_URL)
DB_NAME = os.environ.get("DBNAME", "CaseStudy3")
db: AsyncIOMotorClient = CLIENT[DB_NAME]


class User(BaseModel):
    email: str
    passw: str


def get_db() -> AsyncIOMotorClient:
    return db

def extract_token(bearer_token: str):
    try:
        scheme, token = bearer_token.split()
        if scheme.lower() != 'bearer':
            raise ValueError
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token format",
        )

    return token

async def auth(request: Request,db: AsyncIOMotorClient = Depends(get_db) ): 
    
   
    bearer_token = request.headers.get("Authorization")
    print(f"bearer_token: {bearer_token}")
    
    
    try: 
        if bearer_token is None:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="No access token provided")

        JWT = extract_token(bearer_token)
        print(f"JWT: {JWT}") 

        payload = jwt.decode(JWT, SECRET_KEY, algorithms=ALGORITHM)
        print(f"payload: {payload}")
        exp_time = datetime.fromtimestamp(payload["exp"]).strftime('%Y-%m-%d %H:%M:%S')
        print(f"exp_time: {exp_time}")
        user = await db.users.find_one({"email": payload["sub"]})
        if user:
            return True, None
        else:
            return False, "User not found"
    
    except JWTError as e:
        print(f"Exception occurred: {e}")
        return False, e
    except HTTPException as e:
        print(f"Exception occurred: {e.detail}")
        return False, e.detail



def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()

    if expires_delta is None:
         expire = datetime.now(timezone.utc) + timedelta(minutes=15)
         expire = expire.strftime('%Y-%m-%d %H:%M:%S')
    else :
        expire = expires_delta
    
    print(f"expire: {expire}")
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt




@app.post("/register")
async def register(user: User, request: Request, response: Response, db: AsyncIOMotorClient = Depends(get_db) ):
    
    user_data = user.dict()
    access_token_expires = datetime.now(timezone.utc) + timedelta(minutes=JWT_EXPIRATION_MINUTES)
    access_token = create_access_token(
            data={"sub": f"{user_data['email']}"}, expires_delta=access_token_expires)
    print(f"access_token_expires: {access_token_expires.strftime('%Y-%m-%d %H:%M:%S')}")


    user_data = {**user_data, 
                 "JWT": access_token,
                 }

    print(f"User data before: {user_data}")
    user = await db.users.find_one_and_update({"email": user_data['email']}, {"$set": user_data})
    if user is None:
       

        await db.users.insert_one(user_data)
        response.status_code = status.HTTP_201_CREATED 
        print(f"User {user_data['email']} registered successfully.")
    else :
        print(f"User with {user_data['email']} already exists. Updating expiration of JWT token.")
        response.status_code = status.HTTP_202_ACCEPTED 

    response.set_cookie(key="access_token",value=f"Bearer {access_token}", httponly=True)  # set HttpOnly cookie in response

    return {"access_token": access_token, "token_type": "bearer",}


async def get_random_quote():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://api.quotable.io/random')
        if response.status_code == 200:
            json_response = response.json()
            return {"quote": json_response['content'], "author": json_response['author']}
        else:
            return {"External error": "Unable to fetch random quote"}



@app.get("/hidden_resource")
async def fetch_resource(response: Response, request: Request, auth_approval:tuple[bool,str] = Depends(auth)):

    auth, e = auth_approval
    
    print(f"auth_approval: {auth_approval}")
    print(f"client's ip:{request.client.host}")
    if auth:
        # fetch random quote logic
        random_quote = await get_random_quote()

        return random_quote
    else:
        # write to log file
        requests_logger.critical(f"{e}", extra = {"clientip": request.client.host, 
                                                  "endpoint": request.url.path})
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"message": "Unauthorized access - Warning logged.",
                "details": f"{e}"}


@app.get("/unregister")
async def unregister(response: Response, request: Request, 
                     auth_approval:tuple[bool,str] = Depends(auth),
                     db: AsyncIOMotorClient = Depends(get_db)): 
       
    auth, e = auth_approval
    if auth:
        JWT = extract_token(request.cookies.get("access_token"))
        user = await db.users.find_one_and_delete({"JWT": JWT})
        response.delete_cookie(key="access_token")
        return {"message": f"User {user['email']} unregistered successfully."}
    
    else:
        requests_logger.critical(f"{e}", extra = {"clientip": request.client.host, 
                                                  "endpoint": request.url.path})
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"message": "Unauthorized access - Warning logged.",
                "details": f"{e}"}
             

@app.get("/health")
async def health():
    return {"Health": "Ok"}

