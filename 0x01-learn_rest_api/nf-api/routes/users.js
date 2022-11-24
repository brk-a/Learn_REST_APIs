import express from 'express'
import {createUser, getUsers, getUser, updateUser, deleteUser} from '../controllers/users.js'

const router = express.Router()

/**All routes here begin with `/users` 
 * The first parameter of `router.get()`  simply indicates 
 * what comes after the `/users`
 * Example: `router.get('/', (req, res) ...` tells us that
 * the URL is `https://example.co.ke/users`
*/
router.get('/', getUsers)
router.post('/', createUser)
router.get('/:id', getUser)
router.delete('/:id', deleteUser)
router.patch('/:id', updateUser)

export default router