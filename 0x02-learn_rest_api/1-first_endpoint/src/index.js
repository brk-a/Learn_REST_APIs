let express = require('express')
let personRoute = require('./routes/person')

const PORT = process.env.PORT || 3000

let app = express()

app.use(express.static('public'))
app.use(personRoute)

app.listen(PORT, () => console.info(`Server runs on port ${PORT}`))