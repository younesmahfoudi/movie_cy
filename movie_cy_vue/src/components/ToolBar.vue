<template>
  <div class="button-list">
    <router-link to="/profil">
      <el-button type="warning" class="darkGray" round>Profil</el-button>
    </router-link>

    <router-link to="/">
      <el-button type="warning" class="darkGray" round>Déconnexion</el-button>
    </router-link>
  </div>
  <router-view />
</template>

<style lang="scss">
@import "../assets/constant.scss";

.button-list {
  float: right;
}

.darkGray {
  color: $darkGray;
  margin: 10px;
}
</style>
