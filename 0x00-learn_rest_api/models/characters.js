const mongoose = require('mongoose');
const Schema = mongoose.Schema;

//create a character Schema & model
const CharacterSchema = new Schema({
    name: {
        type: String,
        required: [true, 'Name field is required']
    },
    profession: {
        type: String,
        required: [true, 'Profession field is required']
    },
    available: {
        type: Boolean,
        default: false,
        required: [true, 'Available field is required']
    }

    //will add in geo-location
});

const Character = mongoose.model('character', CharacterSchema);

module.export = Character; 