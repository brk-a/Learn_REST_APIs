let CustomerModel = require('../models/customer-model')
let express = require('express')

let router = express.Router()

/**
 * CRUD -> Create Read Update Delete
 */

//create a new customer
//POST localhost:3000/customer
router.post('/customer', (req, res) => {
    if (!req.body) {
        return res.status(400).send('Body is not available')      
    }

    let model = new CustomerModel(req.body)
    model.save()
        .then(doc => {
            if (!doc || doc.length === 0) {
                return res.status(500).send(doc)
            }

            res.status(201).send(doc)
        })
        .catch(err => res.status(500).json(err))
})

//read data of a customer
//GET localhost:3000/customer/:email
router.get('/customer', (res, req) => {
    if (!req.query.email) {
        return res.status(400).send('Missing URL parameter: email')
    }

    CustomerModel.findOne({
        email: req.query.email
    })
    .then(doc => res.json(doc))
    .catch(err => res.status(500).json(err))
})

//update data of a customer
//PUT localhost:3000/customer/:email
router.put('/customer', (req, res) => {
    if (!req.query.email) {
        return res.sendStatus(400).send('Missing URL parameter: email')
    }

    CustomerModel.findOneAndUpdate({
        email: req.query.email
    }, req.body, {
        new: true
    })
    .then(doc => res.json(doc))
    .catch(err => res.status(500).json(err))
})

//delete data of a customer
//DELETE localhost:3000/customer/:email
router.delete('/customer', (req, res) => {
    if (!req.query.email) {
        res.status(400).send('Missing URL paramater: email')
    }
    
    CustomerModel.findOneAndRemove({
        email: req.query.email
    })
    .then(doc => res.json(doc))
    .catch(err => res.status(500).json(err))
})

module.exports = router