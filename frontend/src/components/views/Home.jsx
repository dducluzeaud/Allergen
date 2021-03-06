import React, { useState } from 'react';
import PropTypes from 'prop-types';

import { makeStyles } from '@material-ui/core/styles';
import { Formik, Form, Field } from 'formik';
import * as Yup from 'yup';

import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import ListItemText from '@material-ui/core/ListItemText';

import SearchInput from 'components/customComponents/form/SearchInput';
import BackgroundImage from 'components/StyledComponents/BackgroundImage';
import Title from 'components/StyledComponents/Title';

const useStyles = makeStyles({
  capitalize: {
    textTransform: 'capitalize',
  },
});

const SearchSchema = Yup.object().shape({
  searchField: Yup.mixed().oneOf(['produit', 'code barre', 'nutriscore']),
  search: Yup.mixed().when('searchField', {
    is: 'code barre',
    then: Yup.number()
      .typeError('Un code barre est uniquement composé de chiffres!')
      .min(8, 'Un code barre a au moins 8 chiffres')
      .required('Le champ ne peut pas être vide 😔'),
    otherwise: Yup.string().required('Le champ ne peut pas être vide 😔'),
  }),
});

const Home = ({ history }) => {
  const classes = useStyles();
  const [menuEl, setMenuEl] = useState(null);
  const searchFields = {
    produit: 'product_name',
    'code barre': 'barcode',
    nutriscore: 'nutriscore',
  };

  const handleSearch = (val) => {
    const { search, searchField } = val;
    const query = searchFields[searchField];

    if (query === 'barcode ') {
      return () => {};
    }

    return history.push({
      pathname: '/products/',
      search: `?${query}=${search}`,
    });
  };

  const handleSearchList = (event) => {
    setMenuEl(event.currentTarget);
  };

  const handleMenuItem = (event, setFieldValue) => {
    setFieldValue('searchField', event.currentTarget.innerText.toLowerCase());
    setMenuEl(null);
  };

  const closeMenuList = () => {
    setMenuEl(null);
  };

  return (
    <BackgroundImage container direction="column" justify="center" align="center">
      <Title>
        Débarrassez vous de vos allergies alimentaires !
        <span role="img" aria-label="smile">
          😁
        </span>
      </Title>
      <Formik
        initialValues={{
          search: '',
          searchField: 'produit',
        }}
        validationSchema={SearchSchema}
        onSubmit={(values, actions) => handleSearch(values, actions)}
      >
        {({ values, setFieldValue }) => (
          <Form>
            <Field
              name="search"
              component={SearchInput}
              onMenuClick={handleSearchList}
              placeholder={`Rechercher par ${values.searchField.toLowerCase()}`}
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
                  <MenuItem key={field} onClick={(event) => handleMenuItem(event, setFieldValue)}>
                    <ListItemText primary={field} className={classes.capitalize} />
                  </MenuItem>
                ))}
              </Menu>
            </Field>
          </Form>
        )}
      </Formik>
    </BackgroundImage>
  );
};

Home.propTypes = {
  history: PropTypes.shape({
    push: PropTypes.func.isRequired,
  }).isRequired,
};

export default Home;
