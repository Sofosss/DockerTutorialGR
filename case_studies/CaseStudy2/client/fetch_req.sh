#!/bin/bash

api_url="https://jsonplaceholder.typicode.com/users"
post_url="${SERVER_NAME}:${SERVER_PORT}/writeToFile"  

# Make the API call to fetch user data
api_response=$(curl -s "$api_url")

if [ $? -eq 0 ]; then
    # Parse JSON data using jq
    users=$(echo "$api_response" | jq -c '.')

    echo "User data fetched successfully:"
    # echo "$json_data"
    
    # Make the POST request using curl with the fetched JSON data

    echo "$users" | jq -c '.[] | {id, name, email, phone}' | while read -r obj; do
        # Perform a request on each sub-object
        echo "Making a request for record: $obj"
        curl -X POST -H "Content-Type: application/json" -d "$obj" "$post_url"


    sleep 2
    done
   


else
    echo "Failed to fetch user data from the JSONPlaceholder API."
    exit 1
fi