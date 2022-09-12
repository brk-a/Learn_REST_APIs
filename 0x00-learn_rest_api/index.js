const express = require('express');
const routes = require('./routes/api');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

// set up express app
const app = express();

// connect to mongodb
mongoose.connect('mongodb://localhost/charactergo');
mongoose.Promise = global.Promise;

// set up body-parser
app.use(bodyParser.json());

//initialise routes
app.use('/api', routes);

//listen for requests
app.listen(process.env.port || 3000, function(){
    console.log('listening for requests...');
});

