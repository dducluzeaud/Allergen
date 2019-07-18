/* eslint-disable react/jsx-filename-extension */
import React from 'react';
import { Route, Switch } from 'react-router-dom';

import Home from 'components/views/Home';
import AdditifTable from 'components/views/AdditifTable';
import ProductsList from 'components/views/ProductsList';
import ProductDetail from 'components/views/ProductDetail';
import ErrorNotFound from 'components/views/ErrorNotFound';

export default (props) => (
  <Switch>
    <Route exact path="/" component={Home} />
    <Route path="/additifs" component={AdditifTable} />
    <Route path="/products" component={ProductsList} />
    <Route path="/product/:barcode" component={ProductDetail} />
    <Route component={ErrorNotFound} />
  </Switch>
);
