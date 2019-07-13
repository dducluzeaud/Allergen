import React, { useContext } from 'react';
import { Formik, Form, Field } from 'formik';
import * as Yup from 'yup';

import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button';

import { makeStyles } from '@material-ui/core/styles';

import { signUp, login } from 'utils/api/User';
import CustomInput from 'components/customComponents/form/CustomInput';
import CenteredModal from '../CenteredModal';
import { UserContext } from '../../../context/userContext';

const useStyles = makeStyles({
  field: {
    marginBottom: '1em',
  },
  button: {
    marginTop: '1em',
  },
});

const SignupSchema = Yup.object().shape({
  username: Yup.string()
    .min(2, "Nom d'utilisateur trop court!")
    .max(70, "Nom d'utilisateur trop court!")
    .required("Nom d'utilisateur requis"),
  email: Yup.string()
    .email('Email invalide')
    .required('Email requis'),
  password: Yup.string()
    .min(8, 'Le mot de passe doit faire au moins 8 caractères')
    .required('Mot de passe requis'),
  passwordConfirmation: Yup.string()
    .oneOf([Yup.ref('password'), null], 'Les mots de passes ne sont pas identiques')
    .required('Le mot de passe doit contenir au moins 8 caractères'),
});

const SignUpModal = (props) => {
  const classes = useStyles();
  const user = useContext(UserContext);

  const handleSignUp = async (data, { setSubmitting, setFieldError }) => {
    try {
      const { onClose } = props;
      await signUp(data);
      await login(data);
      user.loggedIn();
      onClose();
    } catch (error) {
      const { response } = error;
      if (response.status === 400) {
        Object.entries(response.data).forEach(([field, errors]) => {
          errors.map((e) => setFieldError(field, e));
        });
      }
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <CenteredModal {...props}>
      <Typography variant="h6" color="inherit">
        Inscrivez vous!
      </Typography>
      <Formik
        initialValues={{
          username: '',
          email: '',
          password: '',
          passwordConfirmation: '',
        }}
        validationSchema={SignupSchema}
        onSubmit={(values, actions) => handleSignUp(values, actions)}
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
                name="email"
                type="email"
                component={CustomInput}
                className={classes.field}
                placeholder="Email"
              />
              <Field
                name="password"
                type="password"
                component={CustomInput}
                className={classes.field}
                placeholder="Mot de passe"
              />
              <Field
                name="passwordConfirmation"
                type="password"
                component={CustomInput}
                className={classes.field}
                placeholder="Confirmation du mot de passe"
              />
              <Button
                variant="contained"
                size="large"
                color="primary"
                type="submit"
                className={classes.button}
                disabled={isSubmitting}
              >
                {"M'inscrire"}
              </Button>
            </Grid>
          </Form>
        )}
      </Formik>
    </CenteredModal>
  );
};

export default SignUpModal;
