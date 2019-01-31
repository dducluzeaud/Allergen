import API from '@/api/API'
import store from '@/store'
import router from '@/router'

export const login = (payload) => {
  API.post(store.state.endpoints.obtainJWT, payload)
    .then((response) => {
      store.commit('updateToken', response.data.token)
      // get and set auth user
      API.get('/auth/users/me/').then((response) => {
        console.log(response.data)
        store.commit('setAuthUser', {
          authUser: response.data,
          isAuthenticated: true,
        })
        router.push({
          name: 'Profile',
          params: { username: response.data.username },
        })
      })
    })
    .catch((error) => {
      console.log(error)
      console.debug(error)
      console.dir(error)
    })
}
