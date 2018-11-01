import axios from 'axios'
const API_URL = 'http://0.0.0.0:8000/rest-auth/'


export class APIAuthenticateUser {

    async login(username, password) {
        try {
            const url = `${API_URL}login/`
            console.log(username)
            console.log(password)
            return await axios.post(url, {
                username: username,
                password: password
            }).then(response => response.data)
        } catch (error) {
            console.log(error)
            return error
        }
    }
}