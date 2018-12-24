import axios from 'axios'
const API_URL = 'http://0.0.0.0:8000/api/v1'

export class APIServiceProduct {
  async getProducts() {
    const url = `${API_URL}/product/`
    return axios.get(url).then(response => response.data)
  }
}

export class APIServiceNutriment {
  async getNutriments() {
    const url = `${API_URL}/nutriment/`
    return axios.get(url).then(response => response.data)
  }

  async getNutriment(pk) {
    const url = `${API_URL}/nutriment/${pk}`
    return axios.get(url).then(response => response.data)
  }
}

export class APIServiceAdditives {
  async getAdditives(params) {
    try {
      const url = `${API_URL}/additive/?${params}`
      return await axios.get(url).then(response => response.data)
    } catch (error) {
      return error
    }
  }
}
