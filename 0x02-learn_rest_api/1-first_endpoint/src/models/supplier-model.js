let mongoose = require('mongoose')

let SupplierSchema = new mongoose.Schema({
    name: {
        required: true,
        type: /[0-9a-zA-z]+/
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

module.exports = mongoose.model('Supplier', SupplierSchema)