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
      path: "/:id",
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
    {
      path: "/groups",
      name: "groups",
      component: () =>
        import(/* webpackChunkName : "groups" */ "../views/GroupsView.vue"),
    },
    {
      path: "/group",
      name: "group",
      component: () =>
        import(/* webpackChunkName : "group" */ "../views/Group.vue"),
    },
  ],
});

router.beforeEach((to, from, next) => {
  const publicPages = ["/"];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = localStorage.getItem("user");
  // trying to access a restricted page + not logged in
  // redirect to login page
  if (!loggedIn && authRequired) {
    next("/");
  } else {
    next();
  }
});

export default router;
