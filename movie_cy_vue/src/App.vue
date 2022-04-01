<template>
  <router-view :key="$route.fullPath"></router-view>
</template>

<style lang="scss">
@import "src/assets/constant.scss";

html,
body {
  font-family: $font;
  margin: 0px;
  padding: 0px !important;
  height: 100% !important;
}

#app {
  height: 100%;
  padding: 0%;
}

.el-sub-menu__title {
  padding: 0% !important;
  display: flex;
  justify-content: center;
}
</style>
