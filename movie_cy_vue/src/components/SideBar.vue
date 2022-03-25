<template>
  <div class="sidebar-container">
    <el-avatar
      id="photoGroup"
      :style="{ backgroundColor: '#faa427' }"
      :size="150"
      src="./src/components/icon/utilIcon/logo.svg"
    />
    <el-menu
      class="el-menu-vertical-demo"
      :collapse="isCollapse"
      background-color="#5a6075"
      text-color="#faa427"
    >
      <div v-for="(group, index) in groups" :key="group">
        <el-sub-menu :index="index.toString()">
          <template #title>
            <router-link to="movieGroupList">
              <el-icon v-on:click="isCollapse = !isCollapse">
                <el-avatar
                  id="photoGroup"
                  :style="{ backgroundColor: '#faa427' }"
                  :size="25"
                  :src="group.photo"
                />
              </el-icon>
            </router-link>
          </template>
          <el-menu-item-group>
            <template #title>
              <span>Membres du groupe</span>
            </template>
            <el-menu-item
              v-for="(membre, membreIndex) in groups[index].membres"
              :key="membre"
              :index="membreIndex.toString()"
            >
              {{ membre }}
            </el-menu-item>
          </el-menu-item-group>
        </el-sub-menu>
      </div>
      <el-menu-item index="1245">
        <router-link to="groupCreation">
          <el-icon>
            <el-avatar
              id="photoPlus"
              :style="{ backgroundColor: '#faa427' }"
              :size="25"
              src="./src/components/icon/utilIcon/plus.png"
            />
          </el-icon>
        </router-link>
        <template #title>Créer un groupe</template>
      </el-menu-item>
    </el-menu>
    <router-view />
  </div>
</template>

<script lang="ts" setup>
import { ref } from "vue";

const isCollapse = ref(true);
</script>

<script lang="ts">
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

<style lang="scss" scoped>
@import "../assets/constant.scss";

.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}

.el-menu {
  width: 101%;
}

.el-icon {
  width: 100%;
}

.el-avatar {
  --el-avatar-size: 50px !important;
}

.sidebar-container {
  height: 100%;
  position: fixed;
  background-color: $darkGray;
}

.name-groupe {
  visibility: hidden;
}

#photoPlus {
  height: 130%;
  width: 100%;
  max-width: 30px;
}
</style>
