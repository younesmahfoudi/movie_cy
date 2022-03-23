<script setup>
import ToolBar from "../components/ToolBar.vue";
import MovieList from "../components/MovieList.vue";
import SideBar from "../components/SideBar.vue";
</script>

<template>
  <SideBar />
  <div class="content">
    <div class="toolbar">
      <ToolBar />
    </div>
    <div class="form">
      <MovieList />
    </div>
  </div>
</template>

<style scoped>
.toolbar {
  margin-right: 3%;
  height: 50px;
}

.content {
  margin-left: 10%;
  margin-top: 3%;
  margin-bottom: 3%;
  margin-right: 3%;
}
</style>
