<template>
  <div class="modal-card" style="width: auto">
    <header class="modal-card-head">
      <p class="modal-card-title">Êtes vous sûr de vouloir vous déconnecter ?</p>
    </header>
    <footer class="modal-card-foot">
      <button class="button" type="button" @click="$parent.close()">Fermer</button>
      <button class="button is-primary" type="submit" @click.prevent="logout">Se déconnecter</button>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'LogoutModal',
  methods: {
    logout() {
      this.$store.commit('removeToken')
      this.$emit('close')
      this.$router.push({ name: 'Home' })
    }
  }
}
</script>

<style scoped>
</style>
