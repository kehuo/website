<template>
  <pre ref="pseudo-content">
    <slot></slot>
  </pre>
</template>

<script>
import pseudocode from "pseudocode";

export default {
  mounted() {
    pseudocode.renderElement(this.$refs["pseudo-content"], {
      indentSize: "1.5em",
      lineNumber: true
    });
  }
};
</script>

<style lang="scss" scoped>
@import "~pseudocode/build/pseudocode.min.css";
</style>
