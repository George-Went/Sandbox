<template>
  <div>
    {{ info }}
  </div>
</template>

<script>
export default {
  name: "Axios_component",
  data () {
    return {
      info: null
    }
  },
  mounted () {
    axios
      .get("https://api.coindesk.com/v1/bpi/currentprice.json")
      .then(response => (this.info = response));
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
