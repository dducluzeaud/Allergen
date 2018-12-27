<template>
  <div class="profile">
    <h1 class="title">{{authUser}}</h1>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  computed: {
    ...mapGetters(['authUser'])
  }
}
</script>
