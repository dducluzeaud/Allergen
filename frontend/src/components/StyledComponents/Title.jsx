import React from 'react';
import styled from 'styled-components';

const Title = styled.p`
  text-align: center;
  font-size: 3em;
  font-weight: bold;
  color: #255219;
  justify-content: center;
  align-self: center;
`;

export default (props) => <Title {...props} />;
