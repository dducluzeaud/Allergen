import React, { useState } from 'react';
import styled from 'styled-components';
import { Formik, Form, Field } from 'formik';

import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import ListItemText from '@material-ui/core/ListItemText';

import { Grid, OutlinedInput, Button } from '@material-ui/core';

import SearchInput from '../customComponents/form/SearchInput';

const home = require('assets/home.png');

const FlexGrid = styled(Grid)`
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
  background-image: url(${home});
  height: 90vh;
`;

const Input = styled(OutlinedInput)`
  width: 60%;
  align-self: center;
  background-color: #fff;
  border-radius: 60;
`;

const Title = styled.p`
  text-align: center;
  font-size: 3em;
  font-weight: bold;
  color: #255219;
  justify-content: center;
  align-self: center;
`;

const Home = ({ history }) => {
  const [menuEl, setMenuEl] = useState(null);
  const [searchField, setSearchField] = useState('produit');
  const searchFields = {Produit: 'product_name', 'Code barre': 'barcode', Nutriscore: 'nutriscore'};

  const handleSearch = (val, act) => {
    const { search } = val;
    history.push({
      pathname: '/products/',
      search: `${searchFields[searchField].toLowerCase()}=${search.toLowerCase()}`,
    });
  };

  const handleSearchList = (event) => {
    setMenuEl(event.currentTarget);
  };

  const handleMenuItem = (event) => {
    setSearchField(event.currentTarget.innerText);
    setMenuEl(null);
  };

  const closeMenuList = () => {
    setMenuEl(null);
  };

  return (
    <FlexGrid container direction="column" justify="center" align="center">
      <Title>
        Débarrassez vous de vos allergies alimentaires !
        <span role="img" aria-label="smile">
          😁
        </span>
      </Title>
      <Formik
        initialValues={{
          search: '',
          searchField: searchField,
        }}
        onSubmit={(values, actions) => handleSearch(values, actions)}
      >
        {({ isSubmitting }) => (
          <Form>
            <Field
              name="search"
              component={SearchInput}
              onMenuClick={handleSearchList}
              placeholder={`Rechercher par ${searchField.toLowerCase()}`}
            >
              <Menu
                anchorEl={menuEl}
                getContentAnchorEl={null}
                open={Boolean(menuEl)}
                onClose={closeMenuList}
                elevation={0}
                anchorOrigin={{
                  vertical: 'bottom',
                  horizontal: 'left',
                }}
                transformOrigin={{
                  vertical: 'top',
                  horizontal: 'left',
                }}
              >
                {Object.keys(searchFields).map((field) => (
                  <MenuItem onClick={handleMenuItem}>
                    <ListItemText primary={field} />
                  </MenuItem>
                ))}
              </Menu>
            </Field>
          </Form>
        )}
      </Formik>
    </FlexGrid>
  );
};

export default Home;
