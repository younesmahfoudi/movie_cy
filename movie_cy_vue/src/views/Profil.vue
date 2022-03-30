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
</style>
