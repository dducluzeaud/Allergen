import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import styled from 'styled-components';

import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TablePagination from '@material-ui/core/TablePagination';
import TableRow from '@material-ui/core/TableRow';
import TableSortLabel from '@material-ui/core/TableSortLabel';
import Paper from '@material-ui/core/Paper';
import Tooltip from '@material-ui/core/Tooltip';
import { getAdditives } from 'utils/api/APIService';

const PaperRoot = styled(Paper)`
  margin: 20px;
`;

const EnhancedTableHead = ({ order, orderBy, onRequestSort }) => {
  const rows = [
    {
      id: 'risk',
      label: 'Risques',
    },
    {
      id: 'additive_name',
      label: 'Nom',
    },
    {
      id: 'description',
      label: 'Description',
    },
  ];

  const createSortHandler = property => (event) => {
    onRequestSort(event, property);
  };

  return (
    <TableHead>
      <TableRow>
        {rows.map(row => (
          <TableCell
            key={row.id}
            numeric={row.numeric}
            sortDirection={orderBy === row.id ? order : false}
          >
            <Tooltip title="Sort" enterDelay={300}>
              <TableSortLabel
                active={orderBy === row.id}
                direction={order}
                onClick={createSortHandler(row.id)}
              >
                {row.label}
              </TableSortLabel>
            </Tooltip>
          </TableCell>
        ))}
      </TableRow>
    </TableHead>
  );
};

EnhancedTableHead.propTypes = {
  order: PropTypes.string.isRequired,
  orderBy: PropTypes.string.isRequired,
  onRequestSort: PropTypes.func.isRequired,
};

const AdditifTable = () => {
  const [additifs, setAdditives] = useState([]);
  const [count, setCount] = useState(0);
  const [order, setOrder] = useState('asc');
  const [orderBy, setOrderBy] = useState();
  const [page, setPage] = useState(1);
  const [rowsPerPage, setRowsPerPage] = useState(20);

  useEffect(() => {
    const fetchAdditives = async () => {
      const { data } = await getAdditives(page, rowsPerPage, order, orderBy);
      setCount(data.count);
      setAdditives(data.results);
    };
    fetchAdditives();
  }, [rowsPerPage, page, order, orderBy]);

  const emojizeRisk = (risk) => {
    const emoji = {
      0: () => (
        <span role="img" aria-label="red-heart">
          ❤️
        </span>
      ),
      1: () => (
        <span role="img" aria-label="green-heart">
          💚
        </span>
      ),
      2: () => (
        <span role="img" aria-label="check">
          ✅
        </span>
      ),
      3: () => (
        <span role="img" aria-label="heartBroken">
          💔
        </span>
      ),
      4: () => (
        <span role="img" aria-label="forbidden">
          ⛔️
        </span>
      ),
      default: () => null,
    };

    return (emoji[risk] || emoji.default)();
  };

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(event.target.value);
  };

  const handleRequestSort = (event, property) => {
    const isDesc = orderBy === property && order === 'desc';
    setOrder(isDesc ? 'asc' : 'desc');
    setOrderBy(property);
  };

  return (
    <PaperRoot>
      <Table aria-labelledby="tableTitle">
        <EnhancedTableHead
          order={order}
          orderBy={orderBy}
          onRequestSort={handleRequestSort}
          rowCount={additifs.length}
        />
        <TableBody>
          {additifs.map(additif => (
            <TableRow hover onClick={() => {}} role="checkbox" tabIndex={-1} key={additif.id}>
              <TableCell>{emojizeRisk(additif.risk)}</TableCell>
              <TableCell>{additif.additive_name}</TableCell>
              <TableCell>{additif.description}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
      <TablePagination
        rowsPerPageOptions={[20, 50, 100]}
        component="div"
        count={count}
        rowsPerPage={rowsPerPage}
        page={page}
        backIconButtonProps={{
          'aria-label': 'Previous Page',
        }}
        nextIconButtonProps={{
          'aria-label': 'Next Page',
        }}
        onChangePage={handleChangePage}
        onChangeRowsPerPage={handleChangeRowsPerPage}
      />
    </PaperRoot>
  );
};

export default AdditifTable;
