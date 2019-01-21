<template>
  <div>
    <img v-if="nutriscore === 'a'" src="@/assets/img/nutriscore/A.png">
    <img v-else-if="nutriscore === 'c'" src="@/assets/img/nutriscore/C.png">
    <img v-else-if="nutriscore === 'd'" src="@/assets/img/nutriscore/D.png">
    <img v-else-if="nutriscore === 'e'" src="@/assets/img/nutriscore/E.png">
    <img v-else-if="nutriscore === 'b'" src="@/assets/img/nutriscore/B.png">
  </div>
</template>

<script>
export default {
  props: ['nutriscore']
}
</script>

<style scoped>
img {
  width: 50%;
}
</style>