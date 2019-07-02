import React, { useState, useEffect } from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';
import { MuiThemeProvider } from '@material-ui/core/styles';

import theme from 'utils/theme';
import { UserContext } from 'context/userContext';
import { getUser } from 'utils/api/User';
import Routes from './routes';

import NavBar from './components/customComponents/appbar/NavBar';

const App = () => {
  const [logged, setLogged] = useState();

  useEffect(() => {
    const user = getUser();
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
