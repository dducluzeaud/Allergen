import React from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';

const NavLink = styled(Link)`
  text-decoration: none;
  color: #255219;
  align-self: center;
  font-size: 25px;

  &:hover {
    text-decoration: none;
    color: #000;
  }
`;

export default props => <NavLink {...props} />;
