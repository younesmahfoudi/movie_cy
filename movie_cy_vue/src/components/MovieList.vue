<script lang="ts" setup>
import { Check, Star, Delete } from "@element-plus/icons-vue";
import axios from "axios";
</script>

<template>
  <div class="movieContent">
    <div class="movieList">
      <div class="row">
        <div class="movie" v-for="movie in movies.slice(0, 3)" :key="movie">
          <el-card :body-style="{ padding: '0px' }">
            <img :src="movie.image" class="image" />
            <div style="padding: 14px">
              <span>Yummy hamburger</span>
              <div class="bottom">
                <div class="icon">
                  <el-button type="primary" size="large" :icon="Star" circle />
                  <el-button type="success" size="large" :icon="Check" circle />
                  <el-button type="danger" size="large" :icon="Delete" circle />
                </div>
              </div>
            </div>
          </el-card>
        </div>
      </div>
      <div class="row">
        <div class="movie" v-for="movie in movies.slice(3, 6)" :key="movie">
          <el-card :body-style="{ padding: '0px' }">
            <img :src="movie.image" class="image" />
            <div style="padding: 14px">
              <span>Yummy hamburger</span>
              <div class="bottom">
                <div class="icon">
                  <el-button type="primary" size="large" :icon="Star" circle />
                  <el-button type="success" size="large" :icon="Check" circle />
                  <el-button type="danger" size="large" :icon="Delete" circle />
                </div>
              </div>
            </div>
          </el-card>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      movies: null,
    };
  },
  mounted() {
    axios
      .get("http://localhost:8000/movies/")
      .then((response) => (this.movies = response.data.data[0]));
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

@media screen and (max-width: 1050px) and (min-width: 850px) {
  .movie {
    max-width: 14em !important;
  }
}

@media screen and (max-width: 850px) and (min-width: 600px) {
  .movie {
    max-width: 20em !important;
  }
}

@media screen and (max-width: 360px) {
  .movie {
    max-width: 12em !important;
  }
}
</style>
