import { createWebHistory, createRouter } from "vue-router";
import Tests from "./views/Tests.vue";


const routes = [
  {
    path: "/",
    name: "Tests",
    component: Tests,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
