<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p></p>
  </div>
</template>

<script>
// We export the above template and bind a name (helloworld) and a prop (msg)
// that is a string variable
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style></style>
