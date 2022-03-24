<script lang="ts" setup>
import { Check, Star, Delete } from "@element-plus/icons-vue";
</script>

<template>
  <div class="movieContent">
    <h1>TIER LIST</h1>
    <div class="movieList">
      <div class="movie" v-for="movie in movies" :key="movie">
        <img src="/src/components/icon/exempleAffiche.jpg" />
        <div class="icon">
          <el-button type="warning" size="large" :icon="Star" circle />
          <el-button type="success" size="large" :icon="Check" circle />
          <el-button type="danger" size="large" :icon="Delete" circle />
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      movies: [
        {
          id: 1,
          nom: "film 1",
          genre: "horreur",
          date: "10/12/21",
          affiche: "./src/assets/exempleAffiche.jpg",
        },
        {
          id: 2,
          nom: "film 2",
          genre: "fantaisie",
          date: "10/08/21",
          affiche: "./src/assets/exempleAffiche.jpg",
        },
        {
          id: 3,
          nom: "film 3",
          genre: "policier",
          date: "01/01/97",
          affiche: "./src/assets/exempleAffiche.jpg",
        },
        {
          id: 4,
          nom: "film 4",
          genre: "horreur",
          date: "10/12/21",
          affiche: "./src/assets/exempleAffiche.jpg",
        },
        {
          id: 5,
          nom: "film 5",
          genre: "fantaisie",
          date: "10/08/21",
          affiche: "./src/assets/exempleAffiche.jpg",
        },
        {
          id: 6,
          nom: "film 6",
          genre: "policier",
          date: "01/01/97",
          affiche: "./src/assets/exempleAffiche.jpg",
        },
      ],
    };
  },
};
</script>

<style lang="scss" scoped>
@import "../assets/constant.scss";

h1 {
  text-align: center;
}

img {
  width: 100%;
}

.movieList {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  width: 100%;
}

.movie {
  margin-bottom: 20px;
  max-width: 15em;
}

.icon {
  display: flex;
  justify-content: space-evenly;
}

#photoMovie {
  background-color: $yellow;
}
</style>
