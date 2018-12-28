<template>
  <div class="hero-body">
    <div class="container">
      <div v-for="n in 4" :key="n" v-if="products">
        <div class="tile is-ancestor">
          <div
            class="tile is-parent"
            v-for="product in products.slice((n-1) * 4,  4*n)"
            :key="product.id"
          >
            <article class="tile is-child box">
              <div class="columns">
                <div class="column is-4">
                  <figure class="image is-64x64">
                    <img class="image is-rounded is-64x64" :src="product.image_url">
                  </figure>
                </div>
                <div class="column is-8">
                  <p class="title">{{ product.product_name | capitalize }}</p>
                </div>
              </div>
              <img v-if="product.nutrition_grade === 'a'" src="../assets/img/nutriscore/A.png">
              <img v-else-if="product.nutrition_grade === 'b'" src="../assets/img/nutriscore/B.png">
              <img v-else-if="product.nutrition_grade === 'c'" src="../assets/img/nutriscore/C.png">
              <img v-else-if="product.nutrition_grade === 'd'" src="../assets/img/nutriscore/D.png">
              <img v-else-if="product.nutrition_grade === 'e'" src="../assets/img/nutriscore/E.png">
            </article>
          </div>
        </div>
      </div>
      <br>
      <b-pagination :total="numberOfProducts" :current.sync="page"></b-pagination>
    </div>
  </div>
</template>

<script>
import { APIServiceProduct } from '@/api/APIService'

const APIProduct = new APIServiceProduct()

export default {
  data() {
    return {
      products: [],
      numberOfProducts: 0,
      nextPage: '',
      previousPage: '',
      errors: [],
      page: 1,
      perPage: 20
    }
  },
  created() {
    this.getProducts()
  },
  watch: {
    $route: 'getProducts'
  },
  methods: {
    getProducts() {
      const params = [`offset=${(this.page - 1) * 20}`]
      APIProduct.getProducts(params)
        .then(data => {
          this.products = data.results
          this.numberOfProducts = data.count
          this.nextPage = data.next
          this.previousPage = data.previous
          console.log(data.results)
        })
        .catch(error => {
          this.products = []
          this.numberOfProducts = 0
          throw error
        })
    },
    onPageChange(page) {
      console.log(this.page)
      this.page = page
      this.getProducts()
    }
  }
}
</script>

<style scoped>
.title {
  font-size: 1rem;
}

img {
  height: 50px;
}
</style>