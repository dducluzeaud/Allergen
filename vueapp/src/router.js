import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/views/Home.vue'
import About from '@/views/About.vue'
import Products from '@/views/ProductList.vue'
import ProductDetail from '@/views/ProductDetail.vue'
import Nutriment from '@/views/Nutriment.vue'
import Additives from '@/views/Additives.vue'
import Login from '@/components/Login.vue'
import Profile from '@/views/Profile.vue'
import store from '@/store.js'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/about',
      name: 'About',
      component: About,
    },
    {
      path: '/products',
      name: 'ProductList',
      component: Products,
    },
    {
      path: '/product/:barcode',
      name: 'ProductDetail',
      component: ProductDetail,
    },
    {
      path: '/product/:barcode',
      name: 'ProductDetail',
      component: ProductDetail
    },
    {
      path: '/nutriment/:pk/',
      name: 'Nutriment',
      component: Nutriment,
    },
    {
      path: '/additives',
      name: 'Additives',
      component: Additives,
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
    {
      path: '/profile/:username',
      name: 'Profile',
      component: Profile,
      meta: { requiresAuth: true },
    },
    {
      path: '*',
      name: 'NotFound',
      redirect: { name: 'Home' },
    },
  ],
  mode: 'history',
})

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    // this route requires auth, check if logged in
    // if not, redirect to login page.
    if (!store.getters.isAuthenticated) {
      next({
        name: 'Login',
        query: { redirect: to.fullPath },
      })
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router
