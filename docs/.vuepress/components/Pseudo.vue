<template>
  <div ref="pseudo-content">
    <slot></slot>
  </div>
</template>

<script>
export default {
  mounted() {
    pseudocode.renderElement(this.$refs["pseudo-content"], {
      indentSize: "1.5em",
      lineNumber: true
    });
  }
};
</script>
