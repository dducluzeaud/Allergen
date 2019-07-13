import React from 'react';
import PropTypes from 'prop-types';

import { makeStyles } from '@material-ui/core/styles';

import Modal from '@material-ui/core/Modal';

const getModalStyle = () => ({
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
});

const useStyles = makeStyles({
  paper: {
    position: 'absolute',
    width: 400,
    outline: 'none',
    backgroundColor: '#FFF',
    padding: '1em',
    borderRadius: '1em',
  },
});

const CenteredModal = ({ visible, onClose, children }) => {
  // getModalStyle is not a pure function, we roll the style only on the first render
  const [modalStyle] = React.useState(getModalStyle);
  const classes = useStyles();

  return (
    <Modal
      aria-labelledby="simple-modal-title"
      aria-describedby="simple-modal-description"
      open={visible}
      onClose={onClose}
    >
      <div style={modalStyle} className={classes.paper}>
        {children}
      </div>
    </Modal>
  );
};

CenteredModal.propTypes = {
  visible: PropTypes.bool,
  onClose: PropTypes.func,
  children: PropTypes.node.isRequired,
};

CenteredModal.defaultProps = {
  visible: null,
  onClose: null,
};

export default CenteredModal;
