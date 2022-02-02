<template>
  <div class="box">
    <h1>{{ DisplayedText }}</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
      DisplayedText: "Hello George", // Binds to {{ GreetingString }}
    };
  },
};
</script>

<style>
div.box {
  border-style: solid;
}
</style>
