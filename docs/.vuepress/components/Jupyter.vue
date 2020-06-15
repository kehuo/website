<template>
  <div class="jupyter-content">
    <tabs v-if="fileList" @changed="tabChanged">
      <tab v-for="(file, index) in fileList" :key="index" :name="file.name"></tab>
    </tabs>
    <tabs v-else-if="srcPrefix" @changed="filePath=srcPrefix + '/' + $event.tab.name + '.ipynb'">
      <tab v-for="(name, index) in ['python','java']" :key="index" :name="name"></tab>
    </tabs>
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
    fileList: {
      type: Array, // [{name:name,path:path}]
      required: false
    },
    srcPrefix: {
      type: String,
      required: false
    }
  },
  data() {
    return {
      filePath: ""
    };
  },
  methods: {
    resizeIframe() {
      this.$refs.iframe.style.height =
        this.$refs.iframe.contentWindow.document.documentElement.scrollHeight +
        "px";
    },
    tabChanged(selectedTab) {
      for (const file of this.fileList) {
        if (file.name === selectedTab.tab.name) {
          this.filePath = file.path;
          break;
        }
      }
    }
  },
  mounted() {
    window.addEventListener("resize", this.resizeIframe);
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.resizeIframe);
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
