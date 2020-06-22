<template>
  <main class="home" aria-labelledby="main-title">
    <Content class="theme-default-content custom" />
  </main>
</template>

<script>
export default {
  name: "Home",

  computed: {
    data() {
      return this.$page.frontmatter;
    }
  }
};
</script>

<style lang="stylus">
.home {
  padding: $navbarHeight 0 0;
  max-width: $homePageWidth;
  margin: 0px auto;
  display: block;
}

@media (max-width: $MQMobile) {
  .home {
  }
}

@media (max-width: $MQMobileNarrow) {
  .home {
  }
}
</style>
