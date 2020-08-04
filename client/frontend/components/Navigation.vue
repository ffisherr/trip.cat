<template>

  <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
    <a class="navbar-brand" href="/">Главная</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse"
            aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarCollapse">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item">
          <nuxt-link to="/trips" class="nav-link">Путешествия</nuxt-link>
        </li>
        <li class="nav-item">
          <nuxt-link to="/about" class="nav-link">О нас</nuxt-link>
        </li>
        <li class="nav-item">
          <nuxt-link to="/blog" class="nav-link">Блог</nuxt-link>
        </li>
      </ul>
    </div>
  </nav>

</template>

<script>
export default {
  name: "Navigation"
}
</script>

<style scoped>

</style>
