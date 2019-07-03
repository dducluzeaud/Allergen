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

export const signUp = ({ username, email, password }) => API.post('/auth/users/', { username, email, password });

export const logout = () => {
  localStorage.removeItem('accessToken');
  localStorage.removeItem('refreshToken');
};

export const getAccessToken = () => localStorage.getItem('refreshToken');

export const refreshToken = () => {
  const token = localStorage.getItem('refreshToken');
  return API.post('/aut/jwt/refresh/', { token });
};

export const getUser = () => {
  try {
    const token = localStorage.getItem('accessToken');
    return jwtDecode(token);
  } catch (error) {
    return null;
  }
};

export const verifyToken = () => {};
