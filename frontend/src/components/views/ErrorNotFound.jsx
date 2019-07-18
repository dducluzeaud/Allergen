import React from 'react';
import PropTypes from 'prop-types';
import Button from '@material-ui/core/Button';
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';

import BackgroundImage from 'components/StyledComponents/BackgroundImage';
import Title from 'components/StyledComponents/Title';

const useStyle = makeStyles({
  button: {
    width: '20%',
  },
});
const ErrorNotFound = ({ history }) => {
  const classes = useStyle();

  const goBack = () => {
    history.goBack();
  };

  const renderMessage = () => {
    if (history.location.pathname === '/productnotfound') {
      const {
        location: {
          state: { product_name },
        },
      } = history;
      return (
        <Title>
          {`Nous n'avons trouvé aucun résultat pour ${product_name} `}
          <span role="image" aria-label="blush">
            😳
          </span>
        </Title>
      );
    }

    return (
      <>
        <Title>
          Oups!{' '}
          <span role="image" aria-label="Oups">
            😱
          </span>{' '}
          Cette page n'existe pas.
        </Title>
      </>
    );
  };

  return (
    <BackgroundImage container direction="column" justify="center" align="center">
      {renderMessage()}
      <Grid container justify="center">
        <Button className={classes.button} variant="contained" color="primary" onClick={goBack}>
          Retour
        </Button>
      </Grid>
    </BackgroundImage>
  );
};

ErrorNotFound.propTypes = {
  history: PropTypes.shape({}).isRequired,
};

export default ErrorNotFound;
