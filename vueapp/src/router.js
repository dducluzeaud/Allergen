import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/views/Home.vue'
import About from '@/views/About.vue'
import Products from '@/views/ProductList.vue'
import Nutriment from '@/views/Nutriment.vue'
import Additives from '@/views/Additives.vue'
import Login from '@/components/Login.vue'
import Profile from '@/views/Profile.vue'

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
      path: '/products',
      name: 'ProductList',
      component: Products
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
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile
    },
    {
      path: '*',
      name: 'NotFound',
      redirect: {name: 'Home'}
    }
  ],
  mode: 'history',
})

