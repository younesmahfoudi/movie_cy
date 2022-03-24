<template>
  <div class="sidenav">
    <el-menu
      active-text-color="#faa427"
      background-color="#5a6075"
      class="el-menu-vertical-demo"
      default-active="2"
      text-color="#ffffff"
      :style="{ height: '100%' }"
    >
      <div class="logo">
        <router-link to="/">
          <el-menu-item class="logoImg" index="0">
            <el-avatar
              id="photoGroup"
              :style="{ backgroundColor: '#faa427' }"
              shape="square"
              :size="50"
              src="./src/components/icon/utilIcon/logo.png"
            />
          </el-menu-item>
        </router-link>
      </div>
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
        <router-link to="/groupCreation">
          <el-menu-item index="15" class="plus">
            <el-avatar
              id="photoGroup"
              :style="{ backgroundColor: '#faa427' }"
              :size="25"
              src="./src/components/icon/utilIcon/plus.png"
            />
          </el-menu-item>
        </router-link>
      </div>
    </el-menu>
  </div>
  <router-view />
</template>

<script>
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
  height: 100%;
  width: 7%;
  min-width: 40px;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  overflow-x: hidden;
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

@media screen and (max-height: 450px) {
  .sidenav {
    padding-top: 15px;
  }
  .sidenav .el-menu {
    font-size: 18px;
  }
}

@media screen and (height: 320px) {
  .logo {
    size: 10;
  }
}
</style>
