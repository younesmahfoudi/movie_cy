<script setup>
import ProfilManager from "../components/ProfilManager.vue";
import SideBar from "../components/SideBar.vue";
import ToolBar from "../components/ToolBar.vue";
</script>

<template>
  <div>
    <SideBar />
    <div class="content-profil">
      <div class="toolbar-profil">
        <ToolBar />
      </div>
      <div class="form-profil">
        <ProfilManager />
      </div>
    </div>
  </div>
</template>

<style>
.toolbar-profil {
  margin-right: 3%;
  height: 50px;
}

.content-profil {
  margin-left: 56px;
}

.form-profil {
  margin-top: 3%;
}
</style>
