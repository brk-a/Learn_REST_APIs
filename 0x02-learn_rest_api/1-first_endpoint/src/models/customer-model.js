let mongoose = require('mongoose')
// const { required } = require('nodemon/lib/config')

const server = process.env.SERVER
const database = process.env.DATABASE
const user = process.env.USER
const password = process.env.PASSWORD

mongoose.connect(`mongodb://${user}:${password}@${server}/${database}`)

let CustomerSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    email: {
        type: String,
        required: true,
        unique: true
    },
    kraPin: {
        type: /^[0-9a-zA-Z]+$/,
        length: 11,
        unique: true,
        required: true
    },
    balance: Number,
    terms: Number,
    phone: {
        type: /((\+){1}(\d){12})/, //+254701234567
        required: true
    }

})

module.exports = mongoose.model('Customer', CustomerSchema)