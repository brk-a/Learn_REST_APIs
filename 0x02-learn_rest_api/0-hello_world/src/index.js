// console.log('You are in index.js. Hello, world!')

let express = require('express')
let app = express()

const PORT = process.env.PORT || 3000

app.use(express.static('public'))
app.listen(PORT, () => console.info(`Server runs on port ${PORT}`))