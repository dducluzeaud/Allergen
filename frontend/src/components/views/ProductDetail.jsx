import React, { useState, useEffect } from 'react';
import { isEmpty } from 'ramda';
import PropTypes from 'prop-types';
import {
  LinearProgress,
  Card,
  CardMedia,
  Typography,
  Grid,
  Avatar,
  Link,
  Chip,
} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';

import emojizeRisk from 'components/customComponents/emojizeRisk';
import { getProductDetail } from 'utils/api/APIService';
import SimpleCard from 'components/StyledComponents/SimpleCard';

const useStyle = makeStyles({
  card: {
    width: 150,
    margin: 15,
    borderRadius: 75,
  },
  media: {
    height: 150,
  },
  avatar: {
    margin: 15,
    justifyContent: 'center',
    alignItems: 'center',
    height: 50,
    width: 50,
  },
  chip: {
    margin: 2,
  },
  categoryContainer: {
    width: '50%',
  },
  nutriscoreA: { backgroundColor: '#3D8A54' },
  nutriscoreB: { backgroundColor: '#8EC15B' },
  nutriscoreC: { backgroundColor: '#F6CD46' },
  nutriscoreD: { backgroundColor: '#E78C3D' },
  nutriscoreE: { backgroundColor: '#DD5834' },
});

const ProductDetail = ({ match }) => {
  const classes = useStyle();
  const [product, setProduct] = useState(null);

  useEffect(() => {
    const {
      params: { barcode },
    } = match;
    const fetchProduct = async (code) => {
      const {
        data: { results },
      } = await getProductDetail(code);
      setProduct(results.pop());
    };
    fetchProduct(barcode);
  }, []);

  const renderBadge = () => {
    const nutritionGrade = product.nutrition_grade.toUpperCase();
    const grade = {
      A: () => classes.nutriscoreA,
      B: () => classes.nutriscoreB,
      C: () => classes.nutriscoreC,
      D: () => classes.nutriscoreD,
      E: () => classes.nutriscoreE,
    };
    const avatarStyle = grade[nutritionGrade]();

    return (
      <Avatar aria-label="Nutriscore" className={(avatarStyle, classes.avatar)}>
        {nutritionGrade}
      </Avatar>
    );
  };

  const renderCategories = () => {
    const { categories } = product;
    const categoriesList = categories.map(c => c.category_name);

    return (
      <Grid container justify="center" alignItems="center">
        <Grid className={classes.categoryContainer}>
          <Typography variant="h6">Catégories:</Typography>
          {categoriesList.map(category => (
            <Chip
              key={category}
              color="primary"
              variant="outlined"
              size="small"
              label={category}
              className={classes.chip}
            />
          ))}
        </Grid>
      </Grid>
    );
  };

  const renderIngredients = () => {
    const { ingredients } = product;

    if (isEmpty(ingredients)) return null;

    const ingredienstList = ingredients.map(i => ({ name: i.ingredient_name }));

    return <SimpleCard title="Ingrédients" list={ingredienstList} />;
  };

  const renderNutriments = () => {
    const { nutriments } = product;

    if (isEmpty(nutriments)) return null;

    const nutrimentsList = nutriments.map(n => ({
      name: n.nutriment_name,
      quantity: `${parseInt(n.nutriment_quantity, 10)} mg`,
    }));

    return <SimpleCard title="Nutriments" list={nutrimentsList} />;
  };

  const renderVitamines = () => {
    const { vitamins } = product;

    if (isEmpty(vitamins)) return null;

    const vitaminsList = vitamins.map(v => ({
      name: v.vitamin_name,
      quantity: v.quantity,
    }));

    return <SimpleCard title="Vitamines" list={vitaminsList} />;
  };

  const renderAdditives = () => {
    const { additives } = product;

    if (isEmpty(additives)) return null;

    const additivesList = additives.map(a => ({
      name: a.additive_name,
      quantity: emojizeRisk(a.risk),
      description: a.description,
    }));

    return <SimpleCard title="Additifs" list={additivesList} />;
  };

  const renderAllergenes = () => {
    const { allergens } = product;

    if (isEmpty(allergens)) return null;

    const allergensList = allergens.map(a => ({
      name: a.allergen_name,
    }));

    return <SimpleCard title="Allergenes" list={allergensList} />;
  };

  const renderTraces = () => {
    const { traces } = product;

    if (isEmpty(traces)) return null;

    const tracesList = traces.map(t => ({
      name: t.name,
    }));

    return <SimpleCard title="Traces" list={tracesList} />;
  };

  return (
    <>
      {!product ? (
        <LinearProgress variant="indeterminate" />
      ) : (
        <>
          <Grid container display="inline" alignItems="center" justify="center">
            <Typography
              align="center"
              display="block"
              color="primary"
              variant="h3"
              className={classes.title}
            >
              {product.product_name}
            </Typography>
            {renderBadge()}
          </Grid>
          <Grid container display="inline" alignItems="center" justify="center">
            <Card className={classes.card}>
              <CardMedia
                className={classes.media}
                image={product.image_url}
                title={product.product_name}
              />
            </Card>
            <Grid>
              <Typography variant="body1">{`Quantité: ${product.quantity}`}</Typography>
              <Typography variant="body1">{`Code barre: ${product.barcode}`}</Typography>
              <Link href={product.url_off} target="_blank" rel="noreferrer" variant="body1">
                {"Plus d'infos"}
              </Link>
            </Grid>
            {renderCategories()}
            <Grid container display="inline" justify="center">
              {renderIngredients()}
              {renderNutriments()}
              {renderVitamines()}
              {renderAdditives()}
              {renderAllergenes()}
              {renderTraces()}
            </Grid>
          </Grid>
        </>
      )}
    </>
  );
};

ProductDetail.propTypes = {
  match: PropTypes.shape({}).isRequired,
};

export default ProductDetail;
