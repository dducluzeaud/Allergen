import API from 'utils/api/API';

export const login = (
  {
    username,
    password,
  },
) => API.post('/auth/jwt/create/', {
  username,
  password,
});

export const signUp = (
  {
    username,
    email,
    password,
  },
) => API.post('/api/v1/auth/users/', { username, email, password });
