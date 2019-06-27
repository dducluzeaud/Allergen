import React, { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import InputBase from '@material-ui/core/InputBase';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import SearchIcon from '@material-ui/icons/Search';

const useStyles = makeStyles({
  root: {
    padding: '2px 4px',
    display: 'flex',
    alignItems: 'center',
    width: 400,
  },
  input: {
    marginLeft: 8,
    flex: 1,
  },
  iconButton: {
    padding: 10,
  },
});

export default function SearchInput({ onMenuClick, children, field, ...props }) {
  const classes = useStyles();

  return (
    <Paper className={classes.root}>
      {children && (
        <>
          <IconButton className={classes.iconButton} aria-label="Menu-Search" onClick={onMenuClick}>
            <MenuIcon />
          </IconButton>
          {children}
        </>
      )}
      <InputBase
        {...field}
        {...props}
        className={classes.input}
        inputProps={{ 'aria-label': 'Search Google Maps' }}
      />
      <IconButton className={classes.iconButton} aria-label="Search">
        <SearchIcon />
      </IconButton>
    </Paper>
  );
}
