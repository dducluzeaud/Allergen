<template lang="html">
  <form class="login form">
    <div class="modal-card" style="width: auto">
        <header class="modal-card-head">
            <p class="modal-card-title">Login</p>
        </header>
        <section class="modal-card-body">
            <b-field label="email" for="id_email">
                <b-input
                    v-model="email"
                    type="text"
                    placeholder="E-mail"
                    autofocus="autofocus"
                    maxlength="100"
                    id="id_email"
                    required>
                </b-input>
            </b-field>
            <b-field label="username" for="id_username">
                <b-input
                    v-model="username"
                    type="text"
                    placeholder="Username"
                    autofocus="autofocus"
                    maxlength="100"
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
        </section>
        <footer class="modal-card-foot">
            <button class="button" type="button" @click="$parent.close()">Close</button>
            <button class="button is-primary" type="submit" @click.prevent="signUp">S'enregistrer</button>
        </footer>
    </div>
  </form>
</template>

<script>
import API from '@/api/API'
import { login } from '@/api/User'

export default {
  name: 'SignUpModal',
  data() {
    return {
      email: '',
      username: '',
      password: '',
    }
  },
  methods: {
    signUp() {
      const payload = {
        email: this.email,
        username: this.username,
        password: this.password,
      }
      API.post('auth/users/create/', payload).then((response) => {
        if (response.status === 201) {
          const body = new FormData()
          body.append('username', this.username)
          body.append('password', this.password)
          login(payload)
          this.$emit('close')
        }
      })
    },
  },
}
</script>
