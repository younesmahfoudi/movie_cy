import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import Connexion from "../views/Connexion.vue";
import Profil from "../views/Profil.vue";
import GroupCreation from "../views/GroupCreation.vue";
import MovieGroupList from "../views/MovieGroupList.vue";
import Register from "../views/Register.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/connexion",
      name: "connexion",
      component: Connexion,
    },
    {
      path: "/groupCreation",
      name: "création de groupe",
      component: GroupCreation,
    },
    {
      path: "/movieGroupList",
      name: "Liste de film",
      component: MovieGroupList,
    },
    {
      path: "/profil",
      name: "profil",
      component: Profil,
    },
    {
      path: "/register",
      name: "register",
      component: Register,
    },
  ],
});

export default router;
