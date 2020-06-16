<template>
  <div class="jupyter-content">
    <p>
      <a
        :href="'https://mybinder.org/v2/gh/LucienZhang/website-binder/master?filepath=notebooks/'+filePath"
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
          @load="resizeIframe(index)"
        ></iframe>
      </tab>
    </tabs>
    <tabs v-else-if="srcPrefix" @changed="filePath=srcPrefix + '/' + $event.tab.name + '.ipynb'">
      <tab v-for="(name, index) in ['python','java']" :key="index" :name="name">
        <iframe
          v-if="filePath!==''"
          frameborder="no"
          scrolling="no"
          :src="'/nbviewer/localfile/'+filePath"
          :ref="'iframe-'+index"
          @load="resizeIframe(index)"
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
    resizeIframe(index) {
      if (index === undefined) {
        index = this.activeIndex;
      }
      if (index === null) {
        return;
      }
      let e = this.$refs["iframe-" + index][0];
      e.style.height =
        e.contentWindow.document.documentElement.scrollHeight + "px";
    },
    tabChanged(selectedTab) {
      for (const file of this.fileList) {
        if (file.name === selectedTab.tab.name) {
          this.filePath = file.path;
          this.activeIndex = selectedTab.tab.$vnode.data.key;
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
