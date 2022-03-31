<template>
  <div class="button-list">
    <el-button type="warning" class="darkGray" @click="goProfil" round
      >Profil</el-button
    >

    <el-button type="warning" class="darkGray" @click="logout" round
      >Déconnexion</el-button
    >
  </div>
</template>

<script lang="ts">
import router from "../router/index";
import authService from "../services/auth.service";

export default {
  methods: {
    logout() {
      authService.logout();
    },

    goProfil() {
      router.push("/profil");
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
