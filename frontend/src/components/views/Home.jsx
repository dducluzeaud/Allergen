import React from 'react';
import styled from 'styled-components';
import { Grid, Container } from '@material-ui/core';
import NavBar from '../customComponents/NavBar';
import OutlinedInput from '@material-ui/core/OutlinedInput';

const home = require('../../assets/home.png');

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

const Subtitle = styled(Text)`
  color: #255219;
`;

const Home = () => (
  <FlexGrid container direction="column" justify="center" align="center">
    <Title>Débarrassez vous de vos allergies alimentaires ! 😁</Title>
    <Input placeholder="Un aliment? " />
  </FlexGrid>
);

export default Home;
