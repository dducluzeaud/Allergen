import React, { useState, useEffect } from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';
import { MuiThemeProvider } from '@material-ui/core/styles';
import { isNil } from 'ramda';

import theme from 'utils/theme';
import Routes from './routes';

import NavBar from './components/customComponents/appbar/NavBar';
import { getUser } from 'utils/api/User';

const UserContext = React.createContext();

const App = () => {
  const [logged, setLogged] = useState();

  useEffect(() => {
    const user = getUser();
    setLogged(user);
  }, []);

  return (
    <>
      <MuiThemeProvider theme={theme}>
        <CssBaseline />
        <UserContext.Provider>
          <NavBar />
          <Routes />
        </UserContext.Provider>
      </MuiThemeProvider>
    </>
  );
};

export default App;
