import React, { Component } from 'react';

import styled from 'styled-components';

import { AppBar, Grid, IconButton } from '@material-ui/core';
import { Link, withRouter } from 'react-router-dom';

import NavLink from '../StyledComponents/NavLink';

const StyledImage = styled.img`
  padding: 15px;
  width: 5%;
  justify-content: center;
`;

const TopBar = styled(AppBar)`
  position: 'relative';
  boxshadow: 'none';
  borderbottom: 1px solid;
  backgroundcolor: #fff;
  height: 10vh;
`;

const logo = require('../../assets/logo.png');

const NavBar = () => (
  <TopBar position="static" color="default">
    <Grid container alignItems="center">
      <StyledImage src={logo} alt="" />
      <NavLink to="/additifs">Additifs</NavLink>
      <IconButton onClick={() => {}} color="inherit" aria-label="Menu" />
    </Grid>
  </TopBar>
);

export default NavBar;
