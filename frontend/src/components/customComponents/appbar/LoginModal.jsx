import React, { useState } from 'react';
import { Formik, Form, Field } from 'formik';
import PropTypes from 'prop-types';
import * as Yup from 'yup';

import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button';
import { makeStyles } from '@material-ui/core/styles';

import { login } from 'utils/api/User';

import CustomInput from 'components/customComponents/form/CustomInput';
import CenteredModal from '../CenteredModal';

const useStyles = makeStyles({
  field: {
    marginBottom: '1em',
  },
  button: {
    marginTop: '1em',
    marginBottom: '1em',
  },
});

const LoginSchema = Yup.object().shape({
  username: Yup.string().required("Nom d'utilisateur requis"),
  password: Yup.string().required('Mot de passe requis'),
});

const LoginModal = (props) => {
  const classes = useStyles();
  const [error, setError] = useState();

  const handleLogin = async (data, { setSubmitting }) => {
    try {
      const { onClose } = props;
      await login(data);
      onClose();
    } catch (e) {
      console.log(e, 'YOLO');
      const { response } = e;
      if (response.status === 400) setError(response.data.non_field_errors[0]);
      if (response.status === 401) setError('Aucun compte trouvé avec ces informations');
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <CenteredModal {...props}>
      <Typography variant="h6" color="inherit">
        Connecter vous!
      </Typography>
      <Formik
        initialValues={{
          username: '',
          password: '',
        }}
        validationSchema={LoginSchema}
        onSubmit={(values, actions) => handleLogin(values, actions)}
      >
        {({ isSubmitting }) => (
          <Form>
            <Grid container direction="column" justify="center" alignItems="center">
              <Field
                name="username"
                component={CustomInput}
                className={classes.field}
                placeholder="Nom d'utilisateur"
              />
              <Field
                name="password"
                type="password"
                component={CustomInput}
                className={classes.field}
                placeholder="Mot de passe"
              />
              <Button
                variant="contained"
                size="large"
                color="primary"
                type="submit"
                className={classes.button}
                disabled={isSubmitting}
              >
                Me connecter
              </Button>
              {error !== '' && (
                <Typography align="center" variant="body1" color="error">
                  {error}
                </Typography>
              )}
            </Grid>
          </Form>
        )}
      </Formik>
    </CenteredModal>
  );
};

LoginModal.propTypes = {
  onClose: PropTypes.func.isRequired,
};

export default LoginModal;
