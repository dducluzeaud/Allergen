<template lang="html">
  <form class="login form">
    <div class="modal-card" style="width: auto">
        <header class="modal-card-head">
            <p class="modal-card-title">Connexion</p>
        </header>
        <section class="modal-card-body">
            <b-field label="username" for="id_username">
                <b-input
                    v-model="username"
                    type="text"
                    placeholder="Username"
                    autofocus="autofocus"
                    maxlength="150"
                    id="id_username"
                    required>
                </b-input>
            </b-field>
            <b-field label="Password" for="id_password">
                <b-input
                    v-model="password"
                    type="password"
                    placeholder="Password"
                    id="id_password"
                    password-reveal
                    required>
                </b-input>
            </b-field>
          <div class="has-text-centered">Vous n'avez pas de compte ?
            <a href="#" @click="openSignup()">Inscrivez-vous !</a>
          </div>
        </section>
        <footer class="modal-card-foot">
            <button class="button" type="button" @click="$parent.close()">Fermer</button>
            <button class="button is-primary" type="submit" @click.prevent="authenticate">Se connecter</button>
        </footer>
    </div>
  </form>
</template>

<script>
import axios from 'axios'
import SignUpModal from '@/components/SignUp'

export default {
  name: 'LoginModal',
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    openSignup() {
      this.$emit('close')
      this.$modal.open({
        parent: this,
        component: SignUpModal,
        hasModalCArd: true,
        props: {}
      })
    },
    authenticate() {
      const payload = {
        username: this.username,
        password: this.password
      }
      axios
        .post(this.$store.state.endpoints.obtainJWT, payload)
        .then(response => {
          this.$store.commit('updateToken', response.data.token)
          // get and set auth user
          const base = {
            baseURL: this.$store.state.endpoints.baseUrl,
            headers: {
              Authorization: `JWT ${this.$store.state.jwt}`,
              'Content-Type': 'application/json'
            },
            xhrFields: {
              withCredentials: true
            }
          }
          // Even though the authentication returned a user object that can be
          // decoded, we fetch it again. This way we aren't super dependant on
          // JWT and can plug in something else.
          const axiosInstance = axios.create(base)
          axiosInstance({
            url: '/users/me/',
            method: 'get',
            params: {}
          }).then(response => {
            this.$store.commit('setAuthUser', {
              authUser: response.data,
              isAuthenticated: true
            })
            this.$emit('close')
            this.$router.push({
              name: 'Profile',
              params: { username: this.username }
            })
          })
        })
        .catch(error => {
          console.log(error)
          console.debug(error)
          console.dir(error)
        })
    }
  }
}
</script>

<style scoped>
#signup {
  text-align: center;
}
</style>
