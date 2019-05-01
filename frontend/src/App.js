import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import 'typeface-roboto';
import CssBaseline from '@material-ui/core/CssBaseline';

import Routes from './routes';
import moduleName from 'module';

// import TheFooter from './components/customComponents/TheFooter';
import NavBar from './components/customComponents/NavBar';

const App = () => (
  <>
    <CssBaseline />
    <NavBar />
    <Routes />
  </>
);

export default App;
