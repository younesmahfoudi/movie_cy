<script setup>
import ProfilManager from "../components/ProfilManager.vue";
<<<<<<< HEAD
</script>

<template>
  <ProfilManager />
</template>

<style>
=======
import SideBar from "../components/SideBar.vue";
import ToolBar from "../components/ToolBar.vue";
</script>

<template>
  <SideBar />
  <div class="content-profil">
    <div class="toolbar-profil">
      <ToolBar />
    </div>
    <div class="form-profil">
      <ProfilManager />
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
>>>>>>> efd0783ce845f7d992372ac92097879970ae1318
</style>
