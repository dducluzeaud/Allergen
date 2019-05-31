/* eslint-disable react/jsx-filename-extension */
import React from 'react';
import { Route, Switch } from 'react-router-dom';

import Home from './components/views/Home';
import AdditifTable from './components/views/AdditifTable';

export default props => (
  <Switch>
    <Route exact path="/" component={Home} />
    <Route path="/additifs" component={AdditifTable} />
  </Switch>
);
