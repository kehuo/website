<template>
  <div ref="jupyter-content">
    <iframe
      frameborder="no"
      width="100%"
      :src="'https://nbviewer.jupyter.org/github/LucienZhang/website/blob/master/docs/assets/notebooks/'+filePath"
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
  }
};
</script>
