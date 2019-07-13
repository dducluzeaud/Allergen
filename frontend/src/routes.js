/* eslint-disable react/jsx-filename-extension */
import React from 'react';
import { Route, Switch } from 'react-router-dom';

import Home from 'views/Home';
import AdditifTable from 'views/AdditifTable';
import ProductsList from 'views/ProductsList';
import ProductDetail from 'views/ProductDetail';

export default props => (
  <Switch>
    <Route exact path="/" component={Home} />
    <Route path="/additifs" component={AdditifTable} />
    <Route path="/products" component={ProductsList} />
    <Route path="/product/:barcode" component={ProductDetail} />
  </Switch>
);
