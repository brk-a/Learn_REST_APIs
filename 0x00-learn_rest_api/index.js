const express = require('express');
const routes = require('./routes/api');

// set up express app
const app = express();

//initialise routes
app.use('/api', routes);

//listen for requests
app.listen(process.env.port || 3000, function(){
    console.log('listening for requests...');
});

