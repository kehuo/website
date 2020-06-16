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
    <tabs v-if="fileList" @changed="tabChanged">
      <tab v-for="(file, index) in fileList" :key="index" :name="file.name">
        <iframe
          v-if="filePath!==''"
          frameborder="no"
          scrolling="no"
          :src="'/nbviewer/localfile/'+filePath"
          :ref="'iframe-'+index"
          @load="resizeIframe"
        ></iframe>
      </tab>
    </tabs>
    <tabs v-else-if="srcPrefix" @changed="tabChanged">
      <tab v-for="(name, index) in ['python','java']" :key="index" :name="name">
        <iframe
          v-if="filePath!==''"
          frameborder="no"
          scrolling="no"
          :src="'/nbviewer/localfile/'+filePath"
          :ref="'iframe-'+index"
          @load="resizeIframe"
        ></iframe>
      </tab>
    </tabs>
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
      filePath: "",
      activeIndex: null
    };
  },
  methods: {
    resizeIframe() {
      let index = this.activeIndex;
      if (index === null) {
        return;
      }
      let e = this.$refs["iframe-" + index][0];
      e.style.height =
        e.contentWindow.document.documentElement.scrollHeight + "px";
    },
    tabChanged(selectedTab) {
      if (this.fileList) {
        for (const file of this.fileList) {
          if (file.name === selectedTab.tab.name) {
            this.filePath = file.path;
            this.activeIndex = selectedTab.tab.$vnode.data.key;
            break;
          }
        }
      } else if (this.srcPrefix) {
        this.filePath = this.srcPrefix + "/" + selectedTab.tab.name + ".ipynb";
        this.activeIndex = selectedTab.tab.$vnode.data.key;
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
