import axios from 'axios'

const API = axios.create({
  timeout: 1000,
  headers: {
    'Content-Type': 'application/json',
  },
})

export default API
