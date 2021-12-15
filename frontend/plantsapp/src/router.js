import { createWebHistory, createRouter } from "vue-router";
import Plants from "./views/Plants.vue";
import Plant from "./views/Plant.vue";
import Request from "./views/Request.vue";

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
  },
  {
    path: "/request",
    name: "request",
    component: Request,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
