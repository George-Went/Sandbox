import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home";
import Table from "../views/Tables";
import Axios from "../views/Axios";
import ComponentBoard from "../views/ComponentBoard";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/tables",
    name: "Tables",
    component: Table,
  },
  {
    path: "/axios",
    name: "Axios",
    component: Axios,
  },
  {
    path: "/componentBoard",
    name: "ComponentBoard",
    component: ComponentBoard,
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});



export default router;
