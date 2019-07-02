import React from 'react';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/core/styles';

import { ErrorMessage } from 'formik';
import { Paper, InputBase } from '@material-ui/core';

import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import SearchIcon from '@material-ui/icons/Search';

const useStyles = makeStyles({
  root: {
    padding: '2px 4px',
    display: 'flex',
    alignItems: 'center',
    width: 400,
  },
  input: {
    marginLeft: 8,
    flex: 1,
  },
  iconButton: {
    padding: 10,
  },
  error: {
    color: '#FF0000',
  },
});

export default function SearchInput({
  onMenuClick, children, field, ...props
}) {
  const classes = useStyles();

  return (
    <>
      <Paper className={classes.root}>
        {children && (
          <>
            <IconButton
              className={classes.iconButton}
              aria-label="Menu-Search"
              onClick={onMenuClick}
            >
              <MenuIcon />
            </IconButton>
            {children}
          </>
        )}
        <InputBase
          {...field}
          {...props}
          className={classes.input}
          inputProps={{ 'aria-label': 'Search for product, a product category or a nutriscore' }}
        />
        <IconButton className={classes.iconButton} aria-label="Search" type="submit">
          <SearchIcon />
        </IconButton>
      </Paper>
      <ErrorMessage name={field.name} component="span" className={classes.error} />
    </>
  );
}

SearchInput.propTypes = {
  onMenuClick: PropTypes.func.isRequired,
  children: PropTypes.node,
  field: PropTypes.shape({}).isRequired,
};

SearchInput.defaultProps = {
  children: null,
};
