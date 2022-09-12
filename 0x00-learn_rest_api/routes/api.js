const express = require('express');
const Character = require('../models/characters');

// set up express app
const router = express.Router();


//get a list of characters from the db
router.get('/characters', (req, res) => {
    res.send({type: 'GET'});
    // res.end(); // optional
});

//add a character to the db
router.post('/characters', (req, res) => {
    Character.create(req.body).then((character) => {
            res.send(character);
        });
    // res.end(); // optional
});

//update details of a character in db
router.put('/characters/:id', (req, res) => {
    res.send({type: 'PUT'});
    // res.end(); // optional
});

//delete a character from db
router.delete('/characters/:id', (req, res) => {
    res.send({type: 'DELETE'});
    // res.end(); // optional
});

module.exports = router;