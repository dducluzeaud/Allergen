import API from 'utils/api/API';
import jwtDecode from 'jwt-decode';

export const login = async ({ username, password }) => {
  const {
    data: { access, refresh },
  } = await API.post('/auth/jwt/create/', {
    username,
    password,
  });
  localStorage.setItem('accessToken', access);
  localStorage.setItem('refreshToken', refresh);
};

export const signUp = ({ username, email, password }) =>
  API.post('/api/v1/auth/users/', { username, email, password });

export const logout = () => {
  localStorage.removeItem('accessToken');
  localStorage.removeItem('refreshToken');
};

export const getAccessToken = () => {
  return localStorage.getItem('refreshToken');
};

export const refreshToken = () => {
  const refreshToken = localStorage.getItem('refreshToken');
  return API.post('/aut/jwt/refresh/', { refreshToken });
};

export const getUser = () => {
  try {
    const token = localStorage.getItem('accessToken');
    console.log(token);
    const jwt = jwtDecode(token);
    console.log(jwt, 'JWT');
    return jwt;
  } catch (error) {
    return null;
  }
};

export const verifyToken = () => {};
