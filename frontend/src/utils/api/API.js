import axios from 'axios';

const API = axios.create({
  timeout: 1000,
  headers: {
    'Content-Type': 'application/json',
  },
  xhrFields: {
    withCredentials: true,
  },
});

// TODO: use webpack dot env
API.defaults.baseURL = 'http://0.0.0.0:8000/';

// Make Axios play nice with Django CSRF
API.defaults.xsrfCookieName = 'csrftoken';
API.defaults.xsrfHeaderName = 'X-CSRFToken';

const token = localStorage.getItem('token');

if (token) {
  API.defaults.headers.common.Authorization = `JWT ${token}`;
} else {
  delete API.defaults.headers.common.Authorization;
}

export default API;
