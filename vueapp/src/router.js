import Vue from 'vue'
import Router from 'vue-router'

import Home from './views/Home.vue'
import About from './views/About.vue'
import Product from './views/Product.vue'
import Nutriment from './views/Nutriment.vue'
import Additives from './views/Additives.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/about',
      name: 'About',
      component: About
    },
    {
      path: '/product',
      name: 'Product',
      component: Product
    },
    {
      path: '/nutriment/:pk/',
      name: 'Nutriment',
      component: Nutriment
    },
    {
      path: '/additives',
      name: 'Additives',
      component: Additives
    }
  ],
  mode: 'history',
})
