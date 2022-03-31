<script setup>
import GroupManager from "../components/GroupManager.vue";
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
        <GroupManager />
      </div>
    </div>
  </div>
</template>

<style>
.content-profil {
  margin-left: 68px;
}
</style>
