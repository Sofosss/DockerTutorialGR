const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs/promises');

const app = express();
const port = process.env.NODE_PORT || 8891;

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
    const filePath = 'data.json';
    await fs.writeFile(filePath, jsonString);

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