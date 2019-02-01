<template>
  <div class="hero-body">
    <div class="container has-text-centered" v-if="nutrimentDescription">
      <div class="columns is-vcentered">
        <div class="column is-5">
          <figure class="image is-4by3">
            <img :src="nutrimentImage" alt="Description">
          </figure>
        </div>
        <div class="column is-6 is-offset-1">
          <h1 class="title is-2">
            {{nutriment | capitalize}}
            <br>
          </h1>
          <h3 class="is-4 has-text-justified">{{nutrimentDescription}}</h3>
          <br>
          <div v-if="nutrimentQuantityM != nutrimentQuantityF">
            <p>Apport journalier homme: {{nutrimentQuantityM}}</p>
            <p>Apport journalier femme: {{nutrimentQuantityF}}</p>
          </div>
          <div v-else>
            <p>Apport journalier: {{nutrimentQuantityM}}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { APIServiceNutriment } from '@/api/APIService'

const APINutriment = new APIServiceNutriment()

export default {
  data() {
    return {
      nutriment: '',
      nutrimentImage: '',
      nutrimentDescription: '',
      nutrimentQuantityM: '',
      nutrimentQuantityF: ''
    }
  },
  created() {
    // Fethc the data the view is created
    // and the data is already being observed
    this.getNutriment()
  },
  watch: {
    // call again the method if the route changes
    $route: 'getNutriment'
  },
  methods: {
    getNutriment() {
      APINutriment.getNutriment(this.$route.params.pk).then(data => {
        this.nutriment = data.nutriment_name
        this.nutrimentImage = require(`../assets/img/nutriments/${
          data.nutriment_name
        }.jpeg`)
        this.nutrimentDescription = data.description
        this.nutrimentQuantityM = data.daily_quantity_m
        this.nutrimentQuantityF = data.daily_quantity_f
      })
    }
  }
}
</script>
