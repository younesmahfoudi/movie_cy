<script setup>
import ProfilManager from "../components/ProfilManager.vue";
import SideBar from "../components/SideBar.vue";
import ToolBar from "../components/ToolBar.vue";
</script>

<template>
  <SideBar />
  <div class="content">
    <div class="toolbar">
      <ToolBar />
    </div>
    <div class="form">
      <ProfilManager />
    </div>
  </div>
</template>

<style>
.toolbar {
  margin-right: 3%;
  height: 50px;
}

.content {
  margin-left: 10%;
}

@media screen and (max-width: 1050px) and (min-width: 800px) {
  .content {
    margin-left: 15% !important;
  }
}

@media screen and (max-width: 800px) and (min-width: 600px) {
  .content {
    margin-left: 20% !important;
  }
}
</style>
