import axios from 'axios';
import { isNil } from 'ramda';

const API = axios.create({
  timeout: 3000,
  headers: {
    'Content-Type': 'application/json',
  },
  xhrFields: {
    withCredentials: true,
  },
});

API.defaults.baseURL = process.env.API_URL;
API.defaults.xsrfCookieName = 'csrftoken';
API.defaults.xsrfHeaderName = 'X-CSRFToken';

const token = localStorage.getItem('accessToken');

if (token) {
  API.defaults.headers.common.Authorization = `Bearer ${token}`;
} else if (!isNil(API.defaults.headers.common.Authorization)) {
  delete API.defaults.headers.common.Authorization;
}

// TODO: USe api interceptors for 401 and refreshong token

export default API;
