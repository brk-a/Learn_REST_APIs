let express = require('express')
let router = express.Router()

// QueryString -> query property on request object
// localhost:3000/person?key0=value0&key1=value1...&keyN=valueN
router.get('/person', (req, res) => {
    if (req.query.name){
        res.send(`You requested person ${req.query.name}`)
    } else {
    res.send('You have requested no persons')
    }
})

//params property on request object
// localhost:3000/person/insert_param_here
router.get('/person/:name', (req, res) => {
    res.send(`You requested person ${req.params.name}`)
})

//route that throws an error (so error-500.html will be served)
router.get('/error', (req, res) => {
    throw new Error('This error is thrown intentionally.')
})
module.exports = router