const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require("path");


const app = express();
const port = process.env.NODE_PORT || 8891;
const directory = process.env.VOLUME_DIR || "/opt/data_per";
// Middleware to parse JSON in the request body
app.use(bodyParser.json());

// Endpoint for handling POST requests
app.post('/writeToFile', async (req, res) => {
  try {
    // Extract JSON data from the request body
    const jsonData = req.body;

    // Convert JSON to string
    const jsonString = JSON.stringify(jsonData, null, 2);

    // Write to a file (you can customize the file name and path)
    const fileName = 'data.json';

    if (!fs.existsSync(directory)) {
      fs.mkdirSync(directory, { recursive: true });
    }
    
    
    
    const filePath = path.join(directory, fileName);
    await fs.writeFile(filePath, jsonString,{flag: 'a+'}, (err) => {
      if (err) {
        console.error("Error writing to file: ", err);
      }
      else {
        console.log(`Data written to ${filePath} successfully!`);
      }
    });

    // Respond with a success message
    res.status(200).send('Data written to file successfully.');
  } catch (error) {
    console.error(error);
    res.status(500).send('Internal Server Error');
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is listening at http://localhost:${port}`);
});