const express = require('express');

// set up express app
const router = express.Router();


//get a list of characters from the db
router.get('/characters', (req, res) => {
    res.send({type: 'GET'});
    // res.end(); // optional
});

//add a character to the db
router.post('/characters', (req, res) => {
    console.log(req.body);
    res.send({
        type: 'POST',
        name: req.body.name,
        id: req.body.id
    });
    // res.end(); // optional
});

//update details of a character in db
router.put('/characters/:id', (req, res) => {
    res.send({type: 'PUT'});
    // res.end(); // optional
});

//delete a charachter from db
router.delete('/characters/:id', (req, res) => {
    res.send({type: 'DELETE'});
    // res.end(); // optional
});

module.exports = router;