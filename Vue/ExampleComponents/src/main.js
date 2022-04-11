import Vue from "vue";

import App from "./App.vue"; // Import the [main/top] app.vue file 
import router from "./router"; // import the vue-router file

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
