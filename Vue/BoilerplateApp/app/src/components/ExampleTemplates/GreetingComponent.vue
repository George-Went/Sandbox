<template>
  <div>
    <h1>{{ GreetingString }}</h1> 
  </div> 
</template>

<script>
export default {
  data() {
    return {
      GreetingString: "Hello There" // Binds to {{ GreetingString }}
    }
  }
}
</script>

<style>
</style>