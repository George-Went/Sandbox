<template>
  <div class="home">
    <h3>Axios</h3>
    <AxiosComponent/>
  </div>
</template>

<script>
// @ is an alias to /src
import AxiosComponent from "../components/Axios_component.vue";


export default {
  name: "AxiosComponent",
  components: {
    AxiosComponent
  },
};
</script>
