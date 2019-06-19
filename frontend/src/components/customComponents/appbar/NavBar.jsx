import React, { useState } from 'react';
import styled from 'styled-components';

import IconButton from '@material-ui/core/IconButton';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Grid from '@material-ui/core/Grid';
import AccountCircle from '@material-ui/icons/AccountCircle';

import SignUpModal from './SignUpModal';
import LoginModal from './LoginModal';
import NavLink from '../../StyledComponents/NavLink';

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

const NavBar = () => {
  const [visible, setVisible] = useState(false);

  const handleLogin = () => {
    setVisible(true);
  };

  return (
    <Root>
      <TopBar position="static" color="default">
        <Toolbar>
          <Grid container direction="row" alignItems="center">
            <NavLink to="/">
              <StyledImage src="assets/logo.png" alt="" />
            </NavLink>
            <NavLink to="/additifs">Additifs</NavLink>
            <NavLink to="/products">Produits</NavLink>
            <IconButton
              aria-label="Account of current user"
              aria-controls="menu-appbar"
              aria-haspopup="true"
              onClick={handleLogin}
              color="inherit"
            >
              <AccountCircle />
            </IconButton>
            <IconButton onClick={() => {}} color="inherit" aria-label="Menu" />
          </Grid>
        </Toolbar>
      </TopBar>
      {/* <SignUpModal visible={visible} onClose={() => setVisible(false)} /> */}
      <LoginModal visible={visible} onClose={() => setVisible(false)} />
    </Root>
  );
};

export default NavBar;
