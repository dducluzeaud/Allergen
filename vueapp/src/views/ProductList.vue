<template>
  <div class="container">
    <section class="section">
      <b-field>
        <b-input placeholder="No label" rounded></b-input>
      </b-field>
    </section>
    <section class="section">
      <div v-for="n in 4" :key="n" v-if="products">
        <div class="tile is-ancestor">
          <div
            class="tile is-parent"
            v-for="product in products.slice((n-1) * 4,  4*n)"
            :key="product.id"
          >
            <article class="tile is-child box">
              <router-link :to="{name: 'ProductDetail', params: { barcode: product.barcode}}">
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
              </router-link>
              <br>
              <p
                id="allergen"
                v-if="product.allergens.length"
                v-for="allergen in product.allergens"
                :key="allergen.id"
              >Allergène: {{allergen.allergen_name | capitalize}} ❗️</p>
              <p
                id="additives"
                v-if="product.additives.length"
                v-for="additive in product.additives"
                :key="additive.id"
              >{{ (additive.risk > 3) ? `Additif à risque: ${additive.additive_name} ⛔️` : ''}}</p>
              <hr>
              <Nutriscore :nutriscore="product.nutrition_grade"/>
            </article>
          </div>
        </div>
      </div>
      <br>
      <b-pagination
        :total="numberOfProducts"
        :current.sync="page"
        :per-page="perPage"
        @click="console.log(props.current)"
      ></b-pagination>
    </section>
  </div>
</template>

<script>
import { APIServiceProduct } from '@/api/APIService'
import Nutriscore from '@/components/Nutriscore'

const APIProduct = new APIServiceProduct()

export default {
  components: {
    Nutriscore,
  },
  data() {
    return {
      products: [],
      numberOfProducts: 0,
      nextPage: '',
      previousPage: '',
      errors: [],
      page: 1,
      perPage: 20,
    }
  },
  created() {
    this.getProducts()
  },
  watch: {
    $route: 'getProducts',
    page() {
      this.getProducts()
    },
  },

  methods: {
    getProducts() {
      const params = `${(this.page - 1) * 20}`
      APIProduct.getProducts(params)
        .then((data) => {
          this.products = data.results
          this.numberOfProducts = data.count
          this.nextPage = data.next
          this.previousPage = data.previous
        })
        .catch((error) => {
          this.products = []
          this.numberOfProducts = 0
          throw error
        })
    },
  },
}
</script>

<style scoped>
.title {
  font-size: 1rem;
}

img {
  height: 40px;
  width: 90px;
}

#allergen,
#additives {
  color: #d42608;
  font-size: 12px;
}
</style>
