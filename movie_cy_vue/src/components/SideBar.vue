<template>
  <div class="sidebar-container">
    <el-avatar
      class="photo-logo"
      :style="{ backgroundColor: $gray }"
      :size="5"
      src="./src/components/icon/utilIcon/logo.svg"
    />
    <el-menu
      class="el-menu-vertical-demo"
      collapse="true"
      background-color="#5a6075"
      text-color="#faa427"
    >
      <div v-for="(group, index) in groups" :key="group">
        <el-sub-menu class="arrow" :index="index.toString()">
          <template #title>
            <router-link
              :to="{ path: group.id }"
              @click="updateMovieList(group.id)"
            >
              <el-icon>
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
    <router-view :key="$route.name" />
  </div>
</template>

<script lang="ts" setup>
import userService from "../services/userService";
import GroupsService from "../services/GroupsService";
import movieList from "../components/MovieList.vue";
import movieGroupList from "../views/MovieGroupList.vue";
</script>

<script lang="ts">
export default {
  data() {
    return {
      groups: [],
    };
  },
  methods: {
    updateMovieList(id) {
      movieGroupList.computed.key.set(id);
      movieList.methods.getMovies(id);
    },
    async afficherGroupe(user) {
      const token = JSON.parse(localStorage.getItem("user"));
      //On récupère les id des groupes des utilisateurs
      const groupes_id = user.groupes;

      // Pour chaque groupe, on récupère les id des membres
      for (let i = 0; i < groupes_id.length; i++) {
        this.groups[i] = await GroupsService.getGroup(
          JSON.parse(localStorage.getItem("user")),
          groupes_id[i]
        );
        this.groups[i]["nom_membres"] = [];

        for (let j = 0; j < this.groups[i].membres.length; j++) {
          let user = await userService.getSpecificUser(
            token,
            this.groups[i].membres[j]
          );
          this.groups[i]["nom_membres"][j] = user.prenom + " " + user.nom;
        }
      }
    },
  },
  async mounted() {
    const token = JSON.parse(localStorage.getItem("user"));
    let user = await userService.getUser(token);
    this.afficherGroupe(user);
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

<style lang="scss">
.photo-logo > img {
  height: 33% !important;
}

.el-sub-menu .el-sub-menu__icon-arrow {
  position: inherit !important;
  top: 0 !important;
  right: 0 !important;
  margin-top: 0 !important;
}
</style>
