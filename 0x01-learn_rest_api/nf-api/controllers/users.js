import {v4 as uuid4} from 'uuid'

let users = [
    {
        fname: 'Goat',
        lname: 'Matata',
        role: 'Founder',
        organisation: 'The GOAT Podcast',
        id: '2056c58d-8672-48eb-8bd5-faa2daaa6a2a'
    },
    {
        fname: 'Dada',
        lname: 'Ng\'ombe',
        role: 'Founder',
        organisation: 'Chizi About Cheese',
        id: 'bc775a9d-6fbd-4bb4-83e4-5d486576388b'
    },
    {
        fname: 'Kaka',
        lname: 'Sungura',
        role: 'Founder',
        organisation: 'Cunning Capital',
        id: '4d355a95-1ca3-463a-9366-7263e98759cb'
    },
    {
        fname: 'Mzee',
        lname: 'Kobe',
        role: 'Founder',
        organisation: 'GoSlo Golf Tour',
        id: 'f615546c-d247-4bb3-91a5-dd094dede293'
    },
    {
        fname: 'Paka',
        lname: 'the Cat',
        role: 'Founder',
        organisation: 'Catnip & Chill',
        id: 'b965901a-63be-4f1d-8b20-e5c926e9a90f'
    },
    {
        fname: 'Kaka',
        lname: 'Mbwamwitu',
        role: 'Founder',
        organisation: 'Wild Good Boy',
        id: '3adf13a8-1df3-42e6-b993-5cba21627fcf'
    },
    {
        fname: 'Kaka',
        lname: 'Mbweha',
        role: 'Founder',
        organisation: 'Fox News in the Henhouse',
        id: '352481ef-3c88-459e-a94a-832c38285a13'
    },
    {
        fname: 'Kaka',
        lname: 'Dubu',
        role: 'Founder',
        organisation: 'Bear with Me',
        id: 'ac3418fd-7378-4404-84a8-2e54b54f5768'
    }
]

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
    const {fname, lname, role, organisation} = req.body
    const userToUpdate = users.find((user) => user.id === id)

    if (fname) userToUpdate.fname = fname
    if (lname) userToUpdate.lname = lname
    if (role) userToUpdate.role = role
    if (organisation) userToUpdate.organisation = organisation

    res.send(`PATCH request updated id ${userToUpdate.id}`)
}