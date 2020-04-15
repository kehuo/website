<template>
  <div>
    <h1>Hellow hello</h1>
    <p>test p</p>
    <p>maybe more</p>
    <p>{{title}}</p>
    <p>my_other</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: "my title",
      my_other: this.other
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
p {
  color: rebeccapurple;
}
</style>
