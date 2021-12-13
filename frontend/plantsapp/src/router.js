import { createWebHistory, createRouter } from "vue-router";
import Plants from "./views/Plants.vue";
import Plant from "./views/Plant.vue";

const routes = [
  {
    path: "/",
    name: "plants",
    component: Plants,
  },
  {
    path: "/:slug",
    name: "plant",
    component: Plant,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
