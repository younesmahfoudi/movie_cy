<template>
  <el-row class="tac">
    <el-col :span="2.5" class="menu">
      <el-menu
        active-text-color="#faa427"
        background-color="#5a6075"
        class="el-menu-vertical-demo"
        default-active="2"
        text-color="#ffffff"
        :collapse="isCollapse"
        :style="{ height: '100%' }"
      >
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
        <div class="logo">
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
    </el-col>
  </el-row>
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
.tac {
  min-height: 939px;
  max-height: 100%;
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
