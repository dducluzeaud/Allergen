import React, { useState, useContext } from 'react';
import styled from 'styled-components';

import IconButton from '@material-ui/core/IconButton';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';

import AccountCircle from '@material-ui/icons/AccountCircle';
import ExitToApp from '@material-ui/icons/ExitToApp';
import Description from '@material-ui/icons/Description';

import { UserContext } from 'context/userContext';
import { logout } from 'utils/api/User';

import SignUpModal from './SignUpModal';
import LoginModal from './LoginModal';
import NavLink from '../../StyledComponents/NavLink';
import { makeStyles } from '@material-ui/styles';

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

const useStyles = makeStyles({
  link: {
    marginLeft: 10,
  },
});

const NavBar = () => {
  const style = useStyles();
  const [visibleLogin, setVisibleLogin] = useState(false);
  const [visibleSignUp, setVisibleSignUp] = useState(false);
  const [menuEl, setMenuEl] = useState(null);
  const user = useContext(UserContext);

  const handleLogin = () => {
    setVisibleLogin(true);
  };

  const handleSignUp = () => {
    setVisibleSignUp(true);
  };

  const handleMenuList = (event) => {
    setMenuEl(event.currentTarget);
  };

  const handleLogout = () => {
    logout();
    user.logOut();
  };

  const closeMenuList = () => {
    setMenuEl(null);
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
            <NavLink to="/products" className={style.link}>
              Produits
            </NavLink>
          </Grid>
          {user.user ? (
            <>
              <IconButton
                aria-label="Account of current user"
                aria-controls="menu-list-grow"
                aria-haspopup="true"
                onClick={handleMenuList}
                color="inherit"
              >
                <AccountCircle />
              </IconButton>
              <Menu
                anchorEl={menuEl}
                getContentAnchorEl={null}
                open={Boolean(menuEl)}
                onClose={closeMenuList}
                elevation={0}
                anchorOrigin={{
                  vertical: 'bottom',
                  horizontal: 'center',
                }}
                transformOrigin={{
                  vertical: 'top',
                  horizontal: 'center',
                }}
              >
                <MenuItem>
                  <ListItemIcon>
                    <Description />
                  </ListItemIcon>
                  <ListItemText primary="Mon profil" />
                </MenuItem>
                <MenuItem onClick={handleLogout}>
                  <ListItemIcon>
                    <ExitToApp />
                  </ListItemIcon>
                  <ListItemText primary="Déconnexion" />
                </MenuItem>
              </Menu>
            </>
          ) : (
            <>
              <Button color="primary" onClick={handleSignUp}>
                Inscription
              </Button>
              <Button color="primary" onClick={handleLogin} className={style.link}>
                Connexion
              </Button>
            </>
          )}
        </Toolbar>
      </TopBar>
      <SignUpModal visible={visibleSignUp} onClose={() => setVisibleSignUp(false)} />
      <LoginModal visible={visibleLogin} onClose={() => setVisibleLogin(false)} />
    </Root>
  );
};

export default NavBar;
