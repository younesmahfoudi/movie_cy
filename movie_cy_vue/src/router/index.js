import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/groupCreation",
      name: "création de groupe",
      component: () =>
        import(
          /* webpackChunkName : "groupCreation" */ "../views/GroupCreation.vue"
        ),
    },
    {
      path: "/movieGroupList",
      name: "Liste de film",
      component: () =>
        import(
          /* webpackChunkName : "movieGroupList" */ "../views/MovieGroupList.vue"
        ),
    },
    {
      path: "/profil",
      name: "profil",
      component: () =>
        import(/* webpackChunkName : "profil" */ "../views/Profil.vue"),
    },
  ],
});

export default router;
