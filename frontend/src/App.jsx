import React from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';

import Routes from './routes';

import NavBar from './components/customComponents/NavBar';

const App = () => (
  <>
    <CssBaseline />
    <NavBar />
    <Routes />
  </>
);

export default App;
