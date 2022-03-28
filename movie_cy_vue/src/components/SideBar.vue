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
              v-for="(membre, membreIndex) in groups[index].nom_membres"
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
import  axios  from "axios";
const isCollapse = ref(true);
</script>

<script lang="ts">
export default {
  data() {
    return {
      groups: [],
      groupes: [
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
          photo: "./src/components/icon/ThemeIcon/horror.png",
        },
        {
          id: 3,
          nom: "Groupe 3",
          membres: ["Jean", "Bernard", "Louis"],
          admin: "Louis",
          photo: "./src/components/icon/ThemeIcon/drama.png",
        },
      ],
    };
  },
  mounted() {
    axios
      .get("http://localhost:8000/users/62417ab001cbe04ba11a6fc2")
      .then((response) => {
        // On récupère les id des groupes des utilisateurs
        this.groupes_id = response.data.data[0].groupes;
        // Pour chaque groupe, on récupère les id des membres
        for (let i = 0; i < this.groupes_id.length; i++) {
          this.request = "http://localhost:8000/groups/" + this.groupes_id[i];
          axios.get(this.request).then((response) => {
            this.groups[i] = response.data.data[0];
            // Pour chaque membre on récupère leur nom
            for (let j = 0; j < this.groups[i].membres.length; j++){
              this.groups[i]["nom_membres"] = []
              this.request_user_infos =  "http://localhost:8000/users/" + this.groups[i].membres[j];
              axios.get(this.request_user_infos).then((response) => {
                this.groups[i]["nom_membres"][j] = response.data.data[0].prenom + " " + response.data.data[0].nom
              });
            }  
          });
        }
      });
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
