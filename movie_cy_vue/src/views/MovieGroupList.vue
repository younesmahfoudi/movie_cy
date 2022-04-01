<script lang="ts" setup>
import ToolBar from "../components/ToolBar.vue";
import MovieList from "../components/MovieList.vue";
import SideBar from "../components/SideBar.vue";
</script>

<template>
  <div>
    <SideBar />
    <div class="content-movieGroupList">
      <div class="toolbar">
        <ToolBar />
      </div>
      <div class="form">
        <MovieList :key="key.get" />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { ref } from "vue";
export default {
  data() {
    return {
      movieListKey: ref(0),
    };
  },
  computed: {
    key: {
      get() {
        console.log(this.movieListKey);
        return this.movieListKey;
      },
      set(id) {
        this.movieListKey = id;
        console.log(this.movieListKey);
      },
    },
  },
};
</script>

<style scoped>
.toolbar {
  margin-right: 3%;
  height: 50px;
}

.content-movieGroupList {
  margin-left: 68px;
}
</style>
