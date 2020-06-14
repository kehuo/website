<template>
  <div class="jupyter-content">
    <iframe
      frameborder="no"
      scrolling="no"
      :src="'/nbviewer/localfile/'+filePath"
      ref="iframe"
      @load="resizeIframe"
    ></iframe>
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
    resizeIframe() {
      this.$refs.iframe.style.height =
        this.$refs.iframe.contentWindow.document.documentElement.scrollHeight +
        "px";
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
