const express = require('express');
const routes = require('./routes/api');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

// set up express app
const app = express();

// connect to mongodb
mongoose.connect('mongodb://localhost/charactergo');
mongoose.Promise = global.Promise;

//set up static middleware
app.use(express.static('public'));

// set up body-parser middleware
app.use(bodyParser.json());

//initialise routes middleware
app.use('/api', routes);

//set up error handling middleware
app.use((err, req, res, next) => {
    // console.log(err);
    res.status(422).send({error: err.message});
});

//listen for requests
app.listen(process.env.port || 3000, function(){
    console.log('listening for requests...');
});

