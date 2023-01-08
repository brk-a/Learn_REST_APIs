let express = require('express')
let path = require('path')
let bodyParser = require('body-parser')

let personRoute = require('./routes/person')
let customerRoute = require('./routes/customer')

const PORT = process.env.PORT || 3000

let app = express()

app.use(bodyParser.json())

app.use((req, res, next) => {
    console.log(`${new Date().toString()}: ${req.originalUrl}, ${req.body}`)
    // res.send('Use `res` or `next` but not both')
    next()
})
app.use(express.static('public'))
app.use(personRoute)
app.use(customerRoute)

//handler for 404 - Resource Not Found
app.use((req, res, next) => {
    res.status(404).send(`${req.originalUrl} cannot be found.`)
    next()
})

//handler for 500 - Internal Server Error
app.use((err, req, res, next) => {
    console.error(err.stack)
    res.sendFile(path.join(__dirname, '../public/error-500.html'))
})

app.listen(PORT, () => console.info(`Server runs on port ${PORT}`))