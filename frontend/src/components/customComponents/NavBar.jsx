import React, { Component } from 'react';
import styled from 'styled-components';

import IconButton from '@material-ui/core/IconButton';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Grid from '@material-ui/core/Grid';

import NavLink from '../StyledComponents/NavLink';

const Root = styled.div`
  flex-grow: 1;
`;
const StyledImage = styled.img`
  width: 8vh;
  justify-content: center;
  margin-right: 10px;
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
  <Root>
    <TopBar position="static" color="default">
      <Toolbar>
        <Grid container direction="row" alignItems="center">
          <NavLink to="/">
            <StyledImage src={logo} alt="" />
          </NavLink>
          <NavLink to="/additifs">Additifs</NavLink>
          <IconButton onClick={() => {}} color="inherit" aria-label="Menu" />
        </Grid>
      </Toolbar>
    </TopBar>
  </Root>
);

export default NavBar;
