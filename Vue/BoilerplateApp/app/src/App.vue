<template>
  <div id="app">
    <ExampleComponent1></ExampleComponent1>
    <!-- The below code -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App" /> -->
    <TableCompleteExample></TableCompleteExample>
  </div>
</template>

<script>
import ExampleComponent1 from "./components/ExampleTemplates/ExampleComponent1.vue";
// import GreetingComponent from "./components/ExampleTemplates/GreetingComponent.vue";
// import HelloWorld from "./components/HelloWorld.vue";
import TableCompleteExample from "./components/ExampleTemplates/TableCompleteExample.vue";

export default {
  name: "App",
  components: {
    ExampleComponent1,
    TableCompleteExample,
  },
};
</script>

<style lang="scss">
/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */

@import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
@import "../node_modules/bootstrap-vue/dist/bootstrap-vue.css";
@import "./assets/scss/variables.scss";
/*  Bootstrap and its default variables */
@import "../node_modules/bootstrap/scss/bootstrap";
/*  BootstrapVue and its default variables */
@import "../node_modules/bootstrap-vue/src/index.scss";
</style>
