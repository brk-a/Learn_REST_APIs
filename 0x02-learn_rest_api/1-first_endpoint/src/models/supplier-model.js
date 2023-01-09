let mongoose = require('mongoose')

let SupplierSchema = new mongoose.Schema({})

module.exports = mongoose.model('Supplier', SupplierSchema)