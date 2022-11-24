import {v4 as uuid4} from 'uuid'

export const createUser = (req, res) => {
    const newUser = req.body
    users.push({...newUser, id: uuid4()})
    res.send(`User id: ${newUser.id}, ${newUser.fname} ${newUser.lname}, has been added to database`)
}

export const getUsers = (req, res) => {
    console.log(users)
    res.send('You are at `/users`')
}

export const getUser = (req, res) => {
    const {id} = req.params
    const foundUser = users.find((user) => user.id === id)
    res.send(`GET request responded with id ${foundUser.id}`)
}

export const deleteUser = (req, res) => {
    const {id} = req.params
    const users = users.filter((user) => user.id !== id)
    res.send(`DELETE request deleted id ${id}`)
}

export const updateUser = (req, res) => {
    const {id} = req.params
    const {fname, lname, age} = req.body
    const userToUpdate = users.find((user) => user.id === id)

    if (fname) userToUpdate.fname = fname
    if (lname) userToUpdate.lname = lname
    if (age) userToUpdate.age = age

    res.send(`PATCH request updated id ${userToUpdate.id}`)
}