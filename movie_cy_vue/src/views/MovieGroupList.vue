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
