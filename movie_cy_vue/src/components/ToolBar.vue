<template>
  <div class="button-list">
    <router-link to="/profil">
      <el-button type="warning" class="darkGray" round>Profil</el-button>
    </router-link>

    <router-link to="/">
      <el-button type="warning" class="darkGray" @click="logout" round
        >Déconnexion</el-button
      >
    </router-link>
  </div>
</template>

<script lang="ts">
import authService from "../services/authService";

export default {
  methods: {
    logout() {
      authService.logout();
    },
  },
};
</script>

<style lang="scss">
@import "../assets/constant.scss";

.button-list {
  float: right;
}

.darkGray {
  margin: 10px;
}
</style>
