import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    authUser: {},
    isAuthenticated: false,
    jwt: localStorage.getItem('token'),
    endpoints: {
      // TODO: Remove hardcoding of dev endpoints
      obtainJWT: '/auth/jwt/create/',
      refreshJWT: '/auth/jwt/refresh/',
    },
  },
  mutations: {
    setAuthUser(state, { authUser, isAuthenticated }) {
      Vue.set(state, 'authUser', authUser)
      Vue.set(state, 'isAuthenticated', isAuthenticated)
    },
    updateToken(state, newToken) {
      localStorage.setItem('token', newToken)
      state.jwt = newToken
    },
    removeToken(state) {
      localStorage.removeItem('token')
      state.jwt = null
      state.authUser = {}
      state.isAuthenticated = false
    },
  },
  actions: {
    login({ commit }) {
      commit('setAuthUser')
    },
  },
  getters: {
    isAuthenticated: (state) => !!state.jwt,
    authUser: (state) => state,
  },
})
