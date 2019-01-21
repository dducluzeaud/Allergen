<template>
  <div class="container">
    <section class="section">
      <div class="columns">
        <div class="column">
          <img :src="product.image_url">
        </div>
        <div class="column">
          <Nutriscore :nutriscore="product.nutrition_grade"/>
        </div>
      </div>
    </section>
    <section class="section">
      <aside class="menu">
        <div class="columns is-multiline is-centered">
          <div v-if="ingredients.length" class="column is-one-third">
            <p class="menu-label">Ingrédients:</p>
            <ul>
              <li
                v-for="{ingredient_name} in ingredients"
                :key="ingredient_name.id"
              >{{ingredient_name | capitalize}}</li>
            </ul>
          </div>
          <div class="column is-one-third" v-if="additives.length">
            <p class="menu-label">Additifs:</p>
            <ul>
              <li
                v-for="{additiveName, risk} in additives"
                :key="additiveName.id"
              >{{risk | emojizeRisk}} {{ additiveName | capitalize }}</li>
            </ul>
          </div>
          <div class="column is-one-third" v-if="traces.length">
            <p class="menu-label">Traces:</p>
            <div v-for="{trace} in traces" :key="trace.id">{{trace | capitalize}}</div>
          </div>
          <div class="column is-one-third" v-if="vitamins.length">
            <p class="menu-label">Vitamines:</p>
            <div
              v-for="{vitaminName} in vitamins"
              :key="vitaminName.id"
            >{{vitaminName | capitalize}}</div>
          </div>
          <div class="column is-one-third" v-if="nutriments.length">
            <p class="menu-label">Nuriments:</p>
            <div v-for="{nutrimentName, nutrimentQuantity} in nutriments" :key="nutrimentName.id">
              <div v-if="nutrimentQuantity !== 0">
                {{nutrimentName | capitalize}} : {{nutrimentQuantity}}
                <span
                  v-if="nutrimentName === 'énergie'"
                >kCal</span>
                <span v-else>mg</span>
              </div>
            </div>
          </div>
          <div class="column is-one-third" v-if="allergens.length">
            <p class="menu-label">Allergènes:</p>
            <div
              v-for="{allergenName} in allergens"
              :key="allergenName.id"
            >{{allergenName | capitalize}}</div>
          </div>
        </div>
      </aside>
    </section>
  </div>
</template>

<script>
import { APIServiceProduct } from '@/api/APIService'
import Nutriscore from '@/components/Nutriscore'

const APIProductDetail = new APIServiceProduct()

export default {
  components: {
    Nutriscore
  },
  data() {
    return {
      product: {}
    }
  },
  created() {
    this.getProductDetail()
  },
  methods: {
    getProductDetail() {
      APIProductDetail.getProductDetail(this.$route.params.barcode)
        .then(data => {
          this.product = data.results[0]
        })
        .catch(error => {
          this.product = {}
          throw error
        })
    }
  },
  computed: {
    ingredients() {
      return Object.values(this.product.ingredients).map(
        ({ ingredient_name }) => ({
          ingredient_name
        })
      )
    },
    vitamins() {
      return Object.values(this.product.vitamins).map(
        ({
          vitamin_name,
          description,
          daily_quantity_m,
          daily_quantity_f
        }) => ({
          vitaminName: vitamin_name,
          vitaminDesc: description,
          vitaminDalyM: daily_quantity_m,
          vitaminDailyF: daily_quantity_f
        })
      )
    },
    nutriments() {
      return Object.values(this.product.nutriments).map(
        ({ nutriment_name, nutriment_quantity }) => ({
          nutrimentName: nutriment_name,
          nutrimentQuantity: parseInt(nutriment_quantity / 1000, 10)
        })
      )
    },
    additives() {
      return Object.values(this.product.additives).map(
        ({ additive_name, risk, description }) => ({
          additiveName: additive_name,
          risk,
          description
        })
      )
    },
    allergens() {
      return Object.values(this.product.allergens).map(({ allergen_name }) => ({
        allergenName: allergen_name
      }))
    },
    traces() {
      return Object.values(this.product.traces).map(({ name }) => ({
        trace: name
      }))
    }
  }
}
</script>

<style scoped>
.column {
  padding: 25px;
}
</style>