<template>
  <div>
    <h1>Menu</h1>
    <div :class="$style.wrapper">
      <div v-for="item in menu" :key="item.cSlug" :class="$style.block">
        <nuxt-link :to="item.cSlug">
          <p>{{item.cName}}</p>
          <img :src="item.cImage">
        </nuxt-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Navigation",

  props: {
    menu: {
      type: Array,
      default: () => []
    }
  }
}
</script>

<style lang="scss" module>
.wrapper {
  display: flex;
}

.block {
  display: flex;
  flex-direction: column;
}
</style>
