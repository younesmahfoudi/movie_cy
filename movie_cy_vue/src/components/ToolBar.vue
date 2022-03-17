<template>
  <div class="button-list">
    <el-button type="warning" class="darkGray" round>Profil</el-button>
    <el-button type="warning" class="darkGray" round>Déconnexion</el-button>
  </div>
</template>

<style lang="scss">
@import "../assets/constant.scss";

.button-list {
  float: right;
}

.darkGray {
  color: $darkGray;
}
</style>
