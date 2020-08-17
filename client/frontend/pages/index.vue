<template>
  <div>
    <h1>Home trip</h1>
    <Navigation :menu="menu"/>
  </div>
</template>

<script>
import Navigation from "../components/Navigation";
import {mapState} from "vuex";

export default {
  components: {
    Navigation
  },

  async asyncData({app, route, params, error, store}) {
    try {
      await store.dispatch('getMenusList')
    } catch (err) {
      console.log(err)
      return error({
        statusCode: 404,
        message: 'Меню не найдено или сервер не доступен'
      })
    }
  },

  computed: {
    ...mapState({
      menu: 'menusList'
    })
  }
}

</script>

<style scoped>

</style>
