import axios from 'axios';

const ApiClient = axios.create({
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
  xhrFields: {
    withCredentials: true,
  },
});

ApiClient.defaults.baseURL = process.env.API_URL;

// Make Axios play nice with Django CSRF
ApiClient.defaults.xsrfCookieName = 'csrftoken';
ApiClient.defaults.xsrfHeaderName = 'X-CSRFToken';

export default ApiClient;
