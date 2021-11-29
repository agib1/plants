import { createWebHistory, createRouter } from "vue-router";
import Tests from "./views/Tests.vue";


const routes = [
  {
    path: "/",
    name: "tests",
    component: Tests,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
