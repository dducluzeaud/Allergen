import axios from 'axios';
import auth from './User';

const API = axios.create({
  timeout: 3000,
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

const token = localStorage.getItem('accessToken');

if (token) {
  API.defaults.headers.common.Authorization = `Bearer ${token}`;
} else {
  delete API.defaults.headers.common.Authorization;
}

API.interceptors.response.use(
  (response) => response,
  (error) => {
    const { response } = error;
    // if it's not an authentication error return the error
    if (response.status !== 401 && response.data.detail !== '') {
      return Promise.reject(error);
    }
    // Logout user if token refresh didn't work or user is disabled
    if (
      error.config.url == '/aut/jwt/refresh/' ||
      error.response.message == 'Account is disabled.'
    ) {
      logout();
      return new Promise((resolve, reject) => {
        reject(error);
      });
    }

    // Try request again with new token
    return refreshToken()
      .then((token) => {
        // New request with new token
        const config = error.config;
        config.headers['Authorization'] = `Bearer ${token}`;

        return new Promise((resolve, reject) => {
          axios
            .request(config)
            .then((response) => {
              resolve(response);
            })
            .catch((error) => {
              reject(error);
            });
        });
      })
      .catch((error) => {
        return new Promise((resolve, reject) => {
          reject(error);
        });
      });
  },
);

export default API;
