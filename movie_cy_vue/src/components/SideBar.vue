<template>
  <div class="sidenav">
    <el-menu
      active-text-color="#faa427"
      background-color="#5a6075"
      class="el-menu-vertical-demo"
      default-active="2"
      text-color="#ffffff"
      :collapse="isCollapse"
      :style="{ height: '100%' }"
    >
      <router-link to="/">
        <div class="logo">
          <el-menu-item class="logoImg" index="0">
            <el-avatar
              id="photoGroup"
              :style="{ backgroundColor: '#faa427' }"
              shape="square"
              :size="50"
              src="./src/components/icon/utilIcon/logo.png"
            />
          </el-menu-item>
        </div>
      </router-link>
      <div class="logo">
        <router-link to="/movieGroupList">
          <el-menu-item v-for="group in groups" :key="group" index="1">
            <el-avatar
              :key="group"
              id="photoGroup"
              :alt="group.nom"
              :style="{ backgroundColor: '#faa427' }"
              :size="50"
              :src="group.photo"
            />
          </el-menu-item>
        </router-link>
      </div>
      <div class="logo">
        <el-menu-item index="15" class="plus">
          <el-avatar
            id="photoGroup"
            :style="{ backgroundColor: '#faa427' }"
            :size="25"
            src="./src/components/icon/utilIcon/plus.png"
          />
        </el-menu-item>
      </div>
    </el-menu>
  </div>
  <router-view />
</template>

<script>
import { ref } from "vue";

const isCollapse = ref(true);

export { isCollapse };
export default {
  data() {
    return {
      groups: [
        {
          id: 1,
          nom: "groupe 1",
          membres: ["Jean", "Bernard", "Louis"],
          admin: "Bernard",
          photo: "./src/components/icon/ThemeIcon/animation.png",
        },
        {
          id: 2,
          nom: "Groupe 2",
          membres: ["Jean", "Bernard", "Louis"],
          admin: "Bernard",
          photo: "./src/components/icon/ThemeIcon/horreur.png",
        },
        {
          id: 3,
          nom: "Groupe 3",
          membres: ["Jean", "Bernard", "Louis"],
          admin: "Louis",
          photo: "./src/components/icon/ThemeIcon/drame.png",
        },
      ],
    };
  },
};
</script>

<style lang="css" scoped>
.sidenav {
  height: 100%; /* Full-height: remove this if you want "auto" height */
  width: 7%; /* Set the width of the sidebar */
  position: fixed; /* Fixed Sidebar (stay in place on scroll) */
  z-index: 1; /* Stay on top */
  top: 0; /* Stay at the top */
  left: 0;
  overflow-x: hidden; /* Disable horizontal scroll */
  display: flex;
}

#photoGroup {
  filter: contrast(200%);
}

.plus {
  display: flex;
  justify-content: center;
}

.logo {
  padding-top: 10%;
}

.logoImg {
  padding-top: 10%;
  padding-bottom: 10%;
}
</style>
