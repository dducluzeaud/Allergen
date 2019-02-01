import API from './API'

export class APIServiceProduct {
  async getProducts(page) {
    try {
      const url = `/product/?offset=${page}`
      return await API.get(url).then((response) => response.data)
    } catch (error) {
      return error
    }
  }

  async getProductDetail(barcode) {
    try {
      const url = `/product/?barcode=${barcode}`
      return await API.get(url).then((response) => response.data)
    } catch (error) {
      return error
    }
  }
}

export class APIServiceNutriment {
  async getNutriments() {
    const url = `/nutriment/`
    return API.get(url).then((response) => response.data)
  }

  async getNutriment(pk) {
    const url = `/nutriment/${pk}`
    return API.get(url).then((response) => response.data)
  }
}

export class APIServiceAdditives {
  async getAdditives(params) {
    try {
      const url = `/additive/?${params}`
      return await API.get(url).then((response) => response.data)
    } catch (error) {
      return error
    }
  }
}
