import React, { useState, useEffect } from 'react';
import queryString from 'query-string';
import { makeStyles } from '@material-ui/core/styles';

import {
  Card,
  CardActionArea,
  CardMedia,
  CardContent,
  CardActions,
  TablePagination,
  Typography,
  Grid,
  Modal,
} from '@material-ui/core';

import { getProducts } from 'utils/api/APIService';

const useStyles = makeStyles({
  card: {
    width: '15%',
    margin: 15,
  },
  media: {
    height: 100,
  },
  nutriscore: {
    height: 50,
  },
  nutriscoreContainer: {
    justifyContent: 'center',
  },
  pagination: {
    alignSelf: 'flex-end',
    justifyContent: 'center',
  },
});

const ProductsList = ({ location }) => {
  const classes = useStyles();
  const [count, setCount] = useState(20);
  const [page, setPage] = useState(1);
  const [productsPerPage, setProductsPerPage] = useState(20);
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const queryParams = location.search;
    const params = queryString.parse(queryParams);
    const fetchProducts = async () => {
      const {
        data: { count, results },
      } = await getProducts(page, productsPerPage, params);
      setCount(count);
      setProducts(results);
    };
    fetchProducts();
  }, [count, page, productsPerPage]);

  const displayNutriscore = (score) => {
    const nutriscore = {
      a: () => 'assets/nutriscore/A.png',
      b: () => 'assets/nutriscore/B.png',
      c: () => 'assets/nutriscore/C.png',
      d: () => 'assets/nutriscore/D.png',
      e: () => 'assets/nutriscore/E.png',
    };

    return nutriscore[score]();
  };

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event) => {
    setProductsPerPage(event.target.value);
  };

  return (
    <>
      <Grid container direction="row" justify="center" spacing={1}>
        {products.map((product) => (
          <Card className={classes.card}>
            <CardActionArea key={product.id}>
              <CardMedia
                className={classes.media}
                image={product.image_url || 'assets/image-not-found.png'}
                title={product.product_name}
              />
              <CardContent>
                <Typography gutterBottom variant="h6" component="h2" noWrap>
                  {product.product_name}
                </Typography>
                <Typography variant="body2" color="textSecondary" component="p" />
              </CardContent>
            </CardActionArea>
            <CardActions className={classes.nutriscoreContainer}>
              <img
                className={classes.nutriscore}
                src={displayNutriscore(product.nutrition_grade)}
                alt="nutriscore"
              />
            </CardActions>
          </Card>
        ))}
      </Grid>
      {!count > 20 && (
        <TablePagination
          className={classes.pagination}
          count={count}
          rowsPerPageOptions={[20, 50, 100]}
          component="div"
          rowsPerPage={productsPerPage}
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
      )}
    </>
  );
};

export default ProductsList;
