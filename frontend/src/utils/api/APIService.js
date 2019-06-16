import { isNil } from 'ramda';
import API from './API';

/**
 * Products endpoint
 */
export const getProducts = (page, perPage) => {
  const offset = page * perPage;

  return API.get(`product/?offset=${offset}&limit=${perPage}`);
};
export const getProductDetail = barcode => API.get(`product/?barcode=${barcode}`);

/**
 * Nutriments endpoint
 */
export const getNutriments = () => API.get('nutriment/');
export const getNutriment = pk => API.get(`nutriment/${pk}`);

/**
 * Additives endpoint
 */
export const getAdditives = (page, perPage, ordering, order) => {
  if (page === 1 && perPage === 20 && ordering === 'asc' && isNil(order)) {
    return API.get('/additive/');
  }

  const buildUrl = {
    perPage: () => `&limit=${perPage}`,
    ordering: () => `&ordering=${ordering === 'desc' ? `-${order}` : order}`,
  };

  let url = `/additive/?offset=${page * perPage}`;
  if (perPage !== 20) {
    url += buildUrl.perPage();
  }
  if (!isNil(order)) {
    url += buildUrl.ordering();
  }

  return API.get(url);
};
