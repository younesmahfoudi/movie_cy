<script lang="ts" setup>
import { Check, Delete } from "@element-plus/icons-vue";
import FilmDetails from "./FilmDetails.vue";
</script>

<template>
  <div class="movieContent">
    <div class="movieList">
      <div class="row">
        <div
          class="movie"
          v-for="(movie, index) in movies.slice(0, 3)"
          :key="movie"
        >
          <el-card :body-style="{ padding: '0px' }">
            <img :src="movie.image" class="image" />
            <div style="padding: 14px">
              <span>{{ movie.title }}</span>
              <div class="bottom">
                <div class="info">
                  <div class="iconGenre">
                    <div
                      class="iconSpace"
                      v-for="genre in movie.genreList"
                      :key="genre"
                    >
                      <el-avatar
                        id="photoGroup"
                        :style="{ backgroundColor: '#faa427' }"
                        :size="25"
                        :title="genre.key"
                        :src="genre.value"
                      />
                    </div>
                  </div>
                  {{ movie.imDbRating }}
                </div>
                <div class="icon">
                  <FilmDetails />
                  <el-button
                    type="success"
                    title="J'ai vu"
                    size="large"
                    :icon="Check"
                    @click="deleteItem(index)"
                    circle
                  />
                  <el-button
                    type="danger"
                    title="Je n'aime pas"
                    size="large"
                    :icon="Delete"
                    @click="deleteItem(index)"
                    circle
                  />
                </div>
              </div>
            </div>
          </el-card>
        </div>
      </div>
      <div class="row">
        <div
          class="movie"
          v-for="(movie, index) in movies.slice(3, 6)"
          :key="movie"
        >
          <el-card :body-style="{ padding: '0px' }">
            <img :src="movie.image" class="image" />
            <div style="padding: 14px">
              <span>{{ movie.title }}</span>
              <div class="bottom">
                <div class="info">
                  <div class="iconGenre">
                    <div
                      class="iconSpace"
                      v-for="genre in movie.genreList"
                      :key="genre"
                    >
                      <el-avatar
                        id="photoGroup"
                        :style="{ backgroundColor: '#faa427' }"
                        :size="25"
                        :title="genre.key"
                        :src="genre.value"
                      />
                    </div>
                  </div>
                  {{ movie.imDbRating }}
                </div>
                <div class="icon">
                  <FilmDetails />
                  <el-button
                    type="success"
                    title="J'ai vu"
                    size="large"
                    :icon="Check"
                    @click="deleteItem(index + 3)"
                    circle
                  />
                  <el-button
                    type="danger"
                    title="Je n'aime pas"
                    size="large"
                    :icon="Delete"
                    @click="deleteItem(index + 3)"
                    circle
                  />
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
import movieService from "../services/movieService";
import userService from "../services/userService";

export default {
  data() {
    return {
      movies: [],
      user: "",
    };
  },
  async mounted() {
    const token = JSON.parse(localStorage.getItem("user"));
    this.movies = await movieService.getMovies(token);
    console.log(this.movies);
  },
  methods: {
    async deleteItem(index) {
      const token = JSON.parse(localStorage.getItem("user"));
      let user = await userService.getUser(token);

      if (user.films != null) {
        user.films.push(this.movies[index].id);
      } else {
        user.films = [this.movies[index].id];
      }
      console.log(user);
      await userService.updateUser(token, { films: user.films });
      this.movies.splice(index, 1);
      console.log(user);
    },
  },
};
</script>

<style lang="scss" scoped>
@import "../assets/constant.scss";

h1 {
  text-align: center;
}

.image {
  width: 229px;
  height: 328px;
}

.row {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  width: 100%;
}

.movieList {
  display: flex;
  flex-direction: row;
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

.info {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.iconGenre {
  display: flex;
  flex-direction: row;
}

.iconSpace {
  margin: 1px;
}

@media screen and (max-width: 760px) and (min-width: 515px) {
  .movie {
    width: 30em !important;
  }

  .image {
    width: 322px;
    height: 459px;
  }

  .el-card {
    width: 322px !important;
  }

  .movie {
    width: 322px !important;
    max-width: 322px !important;
  }
}

@media screen and (min-width: 1075px) {
  .movie {
    width: 30em !important;
  }

  .image {
    width: 322px;
    height: 459px;
  }

  .el-card {
    width: 322px !important;
  }

  .movie {
    width: 322px !important;
    max-width: 322px !important;
  }
}
</style>
