<template>
  <div id="my-app">

<!--    <header>-->
<!--      <Navigation/>-->
<!--    </header>-->

    <main>
      <div class="content">
        <nuxt/>
      </div>
    </main>


    <footer class="footer">
      <Footer/>
    </footer>

  </div>
</template>

<script>
import Navigation from "../components/Navigation";
import Footer from "~/components/Footer";

export default {

  components: {
    Navigation,
    Footer,
  },

  computed: {
    meta() {
      return [
        {charset: 'utf-8'},
        {
          name: 'viewport',
          content: 'width=device-width, initial-scale=1, maximum-scale=1 shrink-to-fit=no'
        },
        {hid: 'description', name: 'description', content: 'Главная'}
      ]
    }
  },
  head() {
    const canonical = `https://mysite.com${this.$route.path
      .toLowerCase()
      .replace(/\/$/, '')}`
    return {
      meta: [
        ...this.meta

      ],
      script: [
        // { src: 'https://markknol.github.io/console-log-viewer/console-log-viewer.js' }
      ],
      link: [{rel: 'canonical', href: canonical}]
    }
  }
}

</script>

<style>

</style>
