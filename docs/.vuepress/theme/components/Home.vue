<template>
  <main class="home" aria-labelledby="main-title">
    <div class="styled-font">
      <p>I AM</p>
      <span id="typed"></span>
    </div>

    <Content class="theme-default-content custom" />
  </main>
</template>

<script>
import Typed from "typed.js";

export default {
  name: "Home",
  computed: {
    data() {
      return this.$page.frontmatter;
    }
  },
  mounted() {
    new Typed(".home #typed", {
      strings: ["A Coder", "A cooker", "A leaner"],
      typeSpeed: 40,
      loop: true
    });
  }
};
</script>

<style lang="stylus">
.home {
  padding: $navbarHeight 0 0;
  max-width: $homePageWidth;
  margin: 0px auto;
  display: block;

  .styled-font {
    font-size: 65px;
    // color: #FFFFFF;
    // font-family : lulo-clean-w01-one-bold, sans-serif;
  }
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
