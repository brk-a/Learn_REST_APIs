import express from 'express'
import {v4 as uuid4} from 'uuid'

const users = [
    {
        fname: 'Goat',
        lname: 'Matata',
        role: 'Founder',
        organisation: 'The GOAT Podcast',
        id: uuid4()
    },
    {
        fname: 'Dada',
        lname: 'Ng\'ombe',
        role: 'Founder',
        organisation: 'Chizi About Cheese',
        id: uuid4()
    },
    {
        fname: 'Kaka',
        lname: 'Sungura',
        role: 'Founder',
        organisation: 'Cunning Capital',
        id: uuid4()
    },
    {
        fname: 'Mzee',
        lname: 'Kobe',
        role: 'Founder',
        organisation: 'GoSlo Golf Tour',
        id: uuid4()
    },
    {
        fname: 'Paka',
        lname: 'the Cat',
        role: 'Founder',
        organisation: 'Catnip & Chill',
        id: uuid4()
    },
    {
        fname: 'Kaka',
        lname: 'Mbwamwitu',
        role: 'Founder',
        organisation: 'Wild Good Boy',
        id: uuid4()
    },
    {
        fname: 'Kaka',
        lname: 'Mbweha',
        role: 'Founder',
        organisation: 'Fox News in the Henhouse',
        id: uuid4()
    },
    {
        fname: 'Kaka',
        lname: 'Dubu',
        role: 'Founder',
        organisation: 'Bear with Me',
        id: uuid4()
    }
]

const router = express.Router()

/**All routes here begin with `/users` 
 * The first parameter of `router.get()`  simply indicates 
 * what comes after the `/users`
 * Example: `router.get('/', (req, res) ...` tells us that
 * the URL is `https://example.co.ke/users`
*/
router.get('/', (req, res) => {
    console.log(users)
    res.send('You are at `/users`')
})

router.post('/', (req, res) => {
    const new_user = req.body
    users.push({...new_user, id: uuid4()})
    res.send(`User id: ${id}, ${fname} ${lname}, has been added to database`)
})

router.get('/:id')

export default router