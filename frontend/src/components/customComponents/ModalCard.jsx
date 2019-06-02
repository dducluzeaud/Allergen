import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Modal from '@material-ui/core/Modal';
import Button from '@material-ui/core/Button';


const getModalStyle = () => {
  const top = 50;
  const left = 50;

  return {
    top: '50%',
    left: '50%',
    transform: 'translate(50%, -50%)',
  };
};

const useStyles = makeStyles(({
  paper: {
    position: 'absolute',
    width: 400,
    outline: 'none',
  },
}));

function SimpleModal() {
  const [open, setOpen] = React.useState(false);
  // getModalStyle is not a pure function, we roll the style only on the first render
  const [modalStyle] = React.useState(getModalStyle);

  const handleOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };
  const classes = useStyles();

  return (
    <div>
      <Typography gutterBottom>Click to get the full Modal experience!</Typography>
      <Button onClick={handleOpen}>Open Modal</Button>
      <Modal
        aria-labelledby="simple-modal-title"
        aria-describedby="simple-modal-description"
        open={open}
        onClose={handleClose}
      >
        <div style={modalStyle} className={classes.paper}>
          <Typography variant="h6" id="modal-title">
            Text in a modal
          </Typography>
          <Typography variant="subtitle1" id="simple-modal-description">
            Duis mollis, est non commodo luctus, nisi erat porttitor ligula.
          </Typography>
          <SimpleModal />
        </div>
      </Modal>
    </div>
  );
}

export default SimpleModal;
