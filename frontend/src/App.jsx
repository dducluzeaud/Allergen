import React, { useState, useEffect } from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';
import { MuiThemeProvider } from '@material-ui/core/styles';
import { isNil } from 'ramda';


import theme from 'utils/theme';
import Routes from './routes';

import NavBar from './components/customComponents/appbar/NavBar';

const LoggedContext = React.createContext();

const App = () => {
  const [logged, setLogged] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem('token');
    !isNil(token) ? setLogged(true) : setLogged(false);
  }, [logged]);

  return (
    <>
      <MuiThemeProvider theme={theme}>
        <CssBaseline />
        <NavBar />
        <Routes />
      </MuiThemeProvider>
    </>
  );
};

export default App;
