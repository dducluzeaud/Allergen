import React from 'react';
import PropTypes from 'prop-types';
import Input from '@material-ui/core/Input';
import { ErrorMessage } from 'formik';

import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles({
  error: {
    color: '#FF0000',
  },
});

const CustomInput = ({ field, ...props }) => {
  const classes = useStyles();
  return (
    <>
      <Input {...field} {...props} />
      <ErrorMessage name={field.name} component="span" className={classes.error} />
    </>
  );
};

CustomInput.propTypes = {
  field: PropTypes.shape({
    name: PropTypes.string.isRequired,
  }).isRequired,
  form: PropTypes.string.isRequired,
};

export default CustomInput;
