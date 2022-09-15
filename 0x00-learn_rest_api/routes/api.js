const { request } = require('express');
const express = require('express');
const Character = require('../models/characters');

// set up express app
const router = express.Router();


//get a list of characters from the db
router.get('/characters', (req, res, next) => {
    // Character.find({}).then((character) => { res.send(character)});
    Character.geoNear(
        {type: "Point", coordinates:[parseFloat(req.query.lng), parsefloat(req.query.lat)]},
        {maxDistance: 100000, spherical: true}
    ).then((character) => {
        res.send(character);
    });
    // res.end(); // optional
});

//add a character to the db
router.post('/characters', (req, res, next) => {
    Character.create(req.body).then((character) => {
            res.send(character).catch(next);
        });
    // res.end(); // optional
});

//update details of a character in db
router.put('/characters/:id', (req, res, next) => {
    Character.findByIdAndUpdate({_id: req.params.id}, req.body).then(() => {
        Character.findOne({_id: req.params.id}).then((character) => {
            res.send(character);
        });
    });
    // res.end(); // optional
});

//delete a character from db
router.delete('/characters/:id', (req, res, next) => {
    Character.findByIdAndRemove({_id: request.params.id}).then((character) => {
        res.send(character);
    });
    // res.end(); // optional
});

module.exports = router;