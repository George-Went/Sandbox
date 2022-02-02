<template>
  <div class="exampleComponent"> 
    <p>
      Hello {{ msg }}
    </p>
  </div>
</template>

<script>
export default {
  name: 'ExampleComponent', // This is what the component will be referred as in app.js
  props: {
    msg: String // our <h1> message string
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
div.exampleComponent {
    border: solid;
}
</style>
