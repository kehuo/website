<template>
  <div class="jupyter-content">
    <p>
      <a
        :href="'https://mybinder.org/v2/gh/LucienZhang/website-binder/master?filepath=notebooks/'+filePath"
        target="_blank"
      >
        <img src="https://mybinder.org/badge_logo.svg" alt="Binder" />
      </a>
    </p>
    <lazy-component>
      <iframe
        frameborder="no"
        scrolling="no"
        :src="'/nbviewer/localfile/'+filePath"
        @load="resizeIframe"
      ></iframe>
    </lazy-component>
  </div>
</template>

<script>
export default {
  props: {
    filePath: {
      type: String,
      required: true
    }
  },
  methods: {
    resizeIframe(event) {
      let e = event.path[0];
      e.style.height =
        e.contentWindow.document.documentElement.scrollHeight + "px";
    }
  }
};
</script>

<style lang="scss" scoped>
.jupyter-content {
  iframe {
    width: 100%;
    max-width: 1020px; //keep consistent with sytles/palette.styl->$contentWidth - 40px*2 of padding
  }
}
</style>
