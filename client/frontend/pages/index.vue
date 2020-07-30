<template>
  <div>
    <section data-description="bold/cursive">
      <div class="wrapper">
        <h1 class="beta uppercase montserrat regular line-after-heading">
          Trip step by step
        </h1>
        <p class="delta cardo regular italic">
          Wow, what a beautiful sunrise
        </p>
      </div>
    </section>

    <section data-description="thin/bold">
      <div class="wrapper">
        <h1 class="alpha lato thin thick-header-line uppercase ls-small">
          Nice web type
        </h1>
        <p class="mega open-sans bold uppercase">
          Популярные направления
        </p>
      </div>
    </section>

    <section data-description="Add emphasis with color">
      <div class="wrapper">
        <h1 class="mega montserrat bold">
          Походы и путешествия с нами - это <span class="color-emphasis-1">легко и красиво!</span><br>
<!--          And it is here <span class="color-emphasis-1">to stay.</span>-->
        </h1>
      </div>
    </section>

    <section data-description="Thin/Super bold/thin">
      <div class="wrapper">
        <h1 class="gamma lato thin uppercase ls-xlarge">
          Почему именно<br>
          <span class="open-sans tera ls-xlarge bold">МЫ</span><br>
          <span class="epsilon ls-medium">потому что</span>
        </h1>
      </div>
    </section>

    <section data-description="Playing with serifs">
      <div class="wrapper">
        <h1 class="gamma light merriweather italic text-left">
          Наша<br>
          <span class="tera uppercase text-left ls-large vollkorn bold normal">Миссия</span>
        </h1>
      </div>
    </section>

    <section data-description="Super contrast">
      <div class="wrapper">
        <h1 class="delta uppercase thin raleway color-emphasis-2 ls-medium">
          Наша<br>
          <span class="supersize montserrat bold">Команда</span>
        </h1>
      </div>
    </section>

    <section data-description="Vertical text">
      <div class="wrapper">
        <h1 class="mega abril-fatface regular uppercase line-height-small ls-large">
          <span class="delta lato light ls-small">Just</span><br>
          T<br>
          yp<br>
          e<br>
          &amp;<br>
          fu<br>
          n
        </h1>
      </div>
    </section>

    <section data-description="Playful type">
      <div class="wrapper">
        <h1 class="giga bree-serif regular double-header-line">Just Being Playful</h1>
        <p class="delta oswald regular uppercase ls-large">You know you like it</p>
      </div>
    </section>

    <section data-description="Middle flourish">
      <div class="wrapper">
        <h1 class="mega regular ls-large libre-baskerville uppercase color-emphasis-3">
          Just <span class="decorative-span regular ls-small">The</span> Finest
        </h1>
      </div>
    </section>

    <section data-description="Overlay text">
      <div class="wrapper large-wrap">
        <h1 data-text="Wow, what a fine cofee flavor" class="gigantic bold montserrat ls-xlarge uppercase text-overlay">
          Bold type
        </h1>
      </div>
    </section>
  </div>
</template>

<script>
  export default {
    components: {},

    // data() {
    //   return {
    //     msg: ''
    //   }
    // },

    // async asyncData({$axios}) {
    //   let {data} = await $axios.$get('/');
    //   console.log(data)
    //   return {
    //     msg: data.msg
    //   }
    // },

    head() {
      return 'Nuxt + Python = Love';
    }
  }
</script>

<style>

</style>
