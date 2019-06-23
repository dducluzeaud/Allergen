import React, { useState, useEffect } from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';
import { MuiThemeProvider } from '@material-ui/core/styles';
import { isNil } from 'ramda';

import theme from 'utils/theme';
import Routes from './routes';

import { UserContext } from 'context/userContext';

import NavBar from './components/customComponents/appbar/NavBar';
import { getUser } from 'utils/api/User';

const App = () => {
  const [logged, setLogged] = useState();

  useEffect(() => {
    const user = getUser();
    console.log(user, 'APP: user');
    setLogged(user);
  }, []);

  return (
    <MuiThemeProvider theme={theme}>
      <CssBaseline />
      <UserContext.Provider
        value={{
          user: logged,
          logOut: () => setLogged(false),
          loggedIn: () => setLogged(getUser()),
        }}
      >
        <NavBar />
        <Routes />
      </UserContext.Provider>
    </MuiThemeProvider>
  );
};

export default App;
