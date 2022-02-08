<template>
  <div>
    <h3>Hello</h3>
    <Example/>
  </div>
</template>

<script>
// @ is an alias to /src
// You can also use ..
// import HelloWorld from "../components/HelloWorld.vue";
import Example from "../components/Example.vue";

export default {
  name: "Example",
  components: {
    Example
  },
};
</script>

<style scoped>

</style>