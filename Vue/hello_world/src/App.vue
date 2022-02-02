<template>
  <div id="app">
    <h1>Component Examples</h1>
    <ExampleComponent msg="Homer"/> <!-- Our example component from ./components/ExampleComponent.vue -->
    <ExampleComponent msg="Marge"/>
    <ExampleComponent msg="Bart"/>
    <DisplayTable></DisplayTable>
  </div>
</template>


Scripting for components 
<script>
// importing our components 
import ExampleComponent from './components/ExampleComponent.vue'
import DisplayTable from './components/DisplayTable.vue'

// exporting the vue app with the required components
export default {
  name: 'App',
  components: {
    ExampleComponent,
    DisplayTable
  }
}
</script>

CSS Style 
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
