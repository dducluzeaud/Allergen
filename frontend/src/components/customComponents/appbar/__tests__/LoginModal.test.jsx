import React from 'react';
import { shallow } from 'enzyme';
import LoginModal from '../LoginModal';

describe('<LoginModal />', () => {
  it('Match snapshot', () => {
    const loginComp = shallow(<LoginModal />);
    expect(loginComp).toMatchSnapshot();
  });
});
