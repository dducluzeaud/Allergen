<template>
  <div class="profile">
    <h1 class="title">{{user}}</h1>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import jwt_decode from 'jwt-decode'

export default {
  data() {
    return {
      user: this.user,
      email: this.email
    }
  },
  created() {
    const payload = jwt_decode(this.$store.state.jwt)
    this.user = payload.username
    this.email = payload.email
  },
  computed: {
    ...mapGetters(['authUser'])
  }
}
</script>
