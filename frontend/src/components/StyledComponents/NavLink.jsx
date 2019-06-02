import React from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';

const NavLink = styled(Link)`
  text-decoration: none;
  color: #255219;
  font-size: 25px;
  align-self: center
  margin-left: 10px;

  &:hover {
    text-decoration: none;
    color: #000;
  }
`;

export default props => <NavLink {...props} />;
