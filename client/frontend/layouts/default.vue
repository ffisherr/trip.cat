<template>
  <div id="my-app">

    <header>
      <Navigation/>
    </header>

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
  }
}

</script>

<style>
html, body {
  height: 100%;
}

body {
  display: flex;
  flex-direction: column;
}

.content {
  min-height: 90vh;
  flex: 1 0 auto;
}

.footer {
  flex: 0 0 auto;
}

main {
  padding-top: 50px;
}

</style>
