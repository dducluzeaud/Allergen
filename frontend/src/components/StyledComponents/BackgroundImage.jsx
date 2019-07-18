import React from 'react';
import { Grid } from '@material-ui/core';
import styled from 'styled-components';

import home from 'assets/home.png';

const BackgroundImage = styled(Grid)`
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
  background-image: url(${home});
  height: 90vh;
`;

export default (props) => <BackgroundImage {...props} />;
