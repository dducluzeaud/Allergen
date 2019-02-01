import Vue from 'vue'
import App from '@/App.vue'
import router from '@/router'
import store from '@/store'
import axios from 'axios'
import { truncate, upperFirst } from 'lodash'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import '@/assets/css/style.css'

Vue.use(Buefy)
Vue.config.productionTip = false

Vue.filter('capitalize', (value) => {
  if (!value) return ''
  value = value.toString().toLowerCase()
  if (value.length > 36) {
    value = truncate(value, { length: 36, separator: ' ' })
  }
  return upperFirst(value)
})

Vue.filter('emojizeRisk', (risk) => {
  switch (risk) {
    case 0:
      return '✅'
    case 1:
      return '⚠️'
    case 2:
      return '❓'
    case 3:
      return '⁉️'
    case 4:
      return '⛔️'
  }
})

Vue.filter('normalize', (value) => {
  return parseInt(value / 1000, 10)
})

axios.defaults.baseURL = process.env.VUE_APP_ROOT_API

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app')
