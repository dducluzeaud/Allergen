import axios from 'axios'

const API = axios.create({
  timeout: 1000,
  headers: {
    'Content-Type': 'application/json',
  },
  xhrFields: {
    withCredentials: true,
  },
})

API.defaults.baseURL = process.env.VUE_APP_ROOT_API

const token = localStorage.getItem('token')

if (token) {
  API.defaults.headers.common['Authorization'] = `JWT ${token}`
} else {
  delete API.defaults.headers.common['Authorization']
}

export default API
