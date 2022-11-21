import express from 'express'

const users = [
    {
        fname: 'Goat',
        lname: 'Matata',
        role: 'Founder',
        organisation: 'The GOAT Podcast'
    },
    {
        fname: 'Dada',
        lname: 'Ng\'ombe',
        role: 'Founder',
        organisation: 'Chizi About Cheese'
    },
    {
        fname: 'Kaka',
        lname: 'Sungura',
        role: 'Founder',
        organisation: 'Cunning Capital'
    },
    {
        fname: 'Mzee',
        lname: 'Kobe',
        role: 'Founder',
        organisation: 'GoSlo Golf Tour'
    },
    {
        fname: 'Paka',
        lname: 'the Cat',
        role: 'Founder',
        organisation: 'Catnip & Chill'
    },
    {
        fname: 'Kaka',
        lname: 'Mbwamwitu',
        role: 'Founder',
        organisation: 'Wild Good Boy'
    },
    {
        fname: 'Kaka',
        lname: 'Mbweha',
        role: 'Founder',
        organisation: 'Fox News in the Henhouse'
    },
    {
        fname: 'Kaka',
        lname: 'Dubu',
        role: 'Founder',
        organisation: 'Bear with Me'
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

router.post('/')

export default router