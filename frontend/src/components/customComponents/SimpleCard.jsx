import React from 'react';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/core/styles';
import {
  Card,
  Popover,
  Typography,
  List,
  ListItem,
  ListItemText,
  Divider,
} from '@material-ui/core';

const useStyles = makeStyles({
  card: {
    margin: 20,
    minWidth: 275,
  },
  title: {
    marginTop: 15,
    marginLeft: 15,
    fontSize: 14,
    fontWeight: 'bold',
  },
  pos: {
    marginBottom: 12,
  },
  item: {
    textTransform: 'capitalize',
  },
  description: {
    width: 250,
    padding: 15,
  },
});

export default function SimpleCard({ title, list }) {
  const classes = useStyles();
  const [anchorEl, setAnchorEl] = React.useState(null);
  const [openedPopoverName, setOpenedPopoverName] = React.useState(null);

  const handleClick = (event, name) => {
    setAnchorEl(event.currentTarget);
    setOpenedPopoverName(name);
  };

  const handlePopoverClose = () => {
    setAnchorEl(null);
    setOpenedPopoverName(null);
  };

  return (
    <Card className={classes.card}>
      <Typography className={classes.title} color="textSecondary" gutterBottom>
        {title}
      </Typography>
      <List className={classes.root} aria-label="Products element folders">
        {list.map(item => (
          <React.Fragment key={item.name}>
            <Divider />
            <ListItem>
              <ListItemText
                primary={item.name}
                secondary={item.quantity}
                aria-owns={openedPopoverName ? 'mouse-click-popover' : undefined}
                aria-haspopup="true"
                onClick={item.description ? event => handleClick(event, item.name) : null}
              />
              {item.description && (
                <Popover
                  id="mouse-click-popover"
                  open={openedPopoverName === item.name}
                  anchorEl={anchorEl}
                  anchorOrigin={{
                    vertical: 'bottom',
                    horizontal: 'left',
                  }}
                  transformOrigin={{
                    vertical: 'top',
                    horizontal: 'left',
                  }}
                  onClose={handlePopoverClose}
                  disableRestoreFocus
                >
                  <Typography className={classes.description}>{item.description}</Typography>
                </Popover>
              )}
            </ListItem>
          </React.Fragment>
        ))}
      </List>
    </Card>
  );
}

SimpleCard.propTypes = {
  title: PropTypes.string.isRequired,
  list: PropTypes.arrayOf(
    PropTypes.shape({
      name: PropTypes.string.isRequired,
    }),
  ).isRequired,
};
