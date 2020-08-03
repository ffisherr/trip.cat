<template>
  <div id="my-app">
    <Navigation/>
    <main>
      <nuxt/>
    </main>

  </div>
</template>

<script>
  import Navigation from "../components/Navigation";

  export default {
    components: {
      Navigation,
    }
  }

</script>

<style>

</style>
