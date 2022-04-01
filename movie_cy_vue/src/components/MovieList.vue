<script lang="ts" setup>
import { Check, Delete } from "@element-plus/icons-vue";
import FilmDetails from "./FilmDetails.vue";
import movieService from "../services/movieService";
import userService from "../services/userService";
import GroupsService from "../services/GroupsService";
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
              <span
                style="
                  text-overflow: ellipsis;
                  overflow: hidden;
                  white-space: nowrap;
                "
                >{{ movie.title }}</span
              >
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
                  <FilmDetails :movie="movie" :show="showDetails[index]" />
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
              <span
                style="
                  text-overflow: ellipsis;
                  overflow: hidden;
                  white-space: nowrap;
                "
                >{{ movie.title }}</span
              >
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
                  <FilmDetails :movie="movie" :show="showDetails[index + 3]" />
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
export default {
  data() {
    return {
      movies: [],
      showDetails: [false, false, false, false, false, false],
      user: "",
      groupe: {},
    };
  },
  async created() {
    this.getMovies(this.$route.params.id);
  },
  methods: {
    async deleteItem(index) {
      const token = JSON.parse(localStorage.getItem("user"));
      let user = await userService.getUser(token);
      console.log(user);
      if (user.films != null) {
        user.films.push(this.movies[index].id);
      } else {
        user.films = [this.movies[index].id];
      }
      await userService.updateUser(token, { id: user.id, films: user.films });
      this.movies.splice(index, 1);
    },
    async getMovies(id) {
      const token = JSON.parse(localStorage.getItem("user"));
      const genre = [
        {
          genre: "Action",
          vote: 0,
        },
        {
          genre: "Animation",
          vote: 0,
        },
        {
          genre: "Adventure",
          vote: 0,
        },
        {
          genre: "Comedy",
          vote: 0,
        },
        {
          genre: "Biography",
          vote: 0,
        },
        {
          genre: "Documentary",
          vote: 0,
        },
        {
          genre: "Drama",
          vote: 0,
        },
        {
          genre: "Crime",
          vote: 0,
        },
        {
          genre: "Fantasy",
          vote: 0,
        },
        {
          genre: "Film-noir",
          vote: 0,
        },
        {
          genre: "History",
          vote: 0,
        },
        {
          genre: "Horror",
          vote: 0,
        },
        {
          genre: "Musical",
          vote: 0,
        },
        {
          genre: "Family",
          vote: 0,
        },
        {
          genre: "Romance",
          vote: 0,
        },
        {
          genre: "Mystery",
          vote: 0,
        },
        {
          genre: "Sci-fi",
          vote: 0,
        },
        {
          genre: "Sport",
          vote: 0,
        },
        {
          genre: "Thriller",
          vote: 0,
        },
        {
          genre: "War",
          vote: 0,
        },
        {
          genre: "Western",
          vote: 0,
        },
      ];
      const genreFlex = [
        {
          genre: "Action",
          vote: 0,
        },
        {
          genre: "Animation",
          vote: 0,
        },
        {
          genre: "Adventure",
          vote: 0,
        },
        {
          genre: "Comedy",
          vote: 0,
        },
        {
          genre: "Biography",
          vote: 0,
        },
        {
          genre: "Documentary",
          vote: 0,
        },
        {
          genre: "Drama",
          vote: 0,
        },
        {
          genre: "Crime",
          vote: 0,
        },
        {
          genre: "Fantasy",
          vote: 0,
        },
        {
          genre: "Film-noir",
          vote: 0,
        },
        {
          genre: "History",
          vote: 0,
        },
        {
          genre: "Horror",
          vote: 0,
        },
        {
          genre: "Musical",
          vote: 0,
        },
        {
          genre: "Family",
          vote: 0,
        },
        {
          genre: "Romance",
          vote: 0,
        },
        {
          genre: "Mystery",
          vote: 0,
        },
        {
          genre: "Sci-fi",
          vote: 0,
        },
        {
          genre: "Sport",
          vote: 0,
        },
        {
          genre: "Thriller",
          vote: 0,
        },
        {
          genre: "War",
          vote: 0,
        },
        {
          genre: "Western",
          vote: 0,
        },
      ];
      const filmVu = ["1"];
      const actor = [""];
      let url = "http://localhost:8000/movies/";
      this.groupe = await GroupsService.getGroup(token, id);

      await this.groupe.membres.forEach(async (element, index) => {
        const user = await userService.getSpecificUser(token, element);
        if (user.acteur != null) {
          actor.push(user.acteur);
        }
        if (user.realisateur != null) {
          actor.push(user.realisateur);
        }
        if (user.films != null) {
          user.films.forEach((element) => filmVu.push(element));
        }
        actor.push(user.acteur);
        genre.forEach((e) => {
          if (user.genre == e.genre) {
            e.vote += 1;
          }
        });
        genreFlex.forEach((e) => {
          if (user.genreFlex == e.genre) {
            e.vote += 1;
          }
        });
        if (index === this.groupe.membres.length - 1) {
          genre.sort(function compare(a, b) {
            if (a.vote < b.vote) return 1;
            if (a.vote > b.vote) return -1;
            return 0;
          });
          genreFlex.sort(function compare(a, b) {
            if (a.vote < b.vote) return 1;
            if (a.vote > b.vote) return -1;
            return 0;
          });
          url += `?genrelist=${genre[0].genre}&genrelist=${genreFlex[0].genre}&imdbrating=8`;
          actor.forEach((element, indexActor) => {
            url += `&starlist=${element}`;
            if (indexActor == actor.length - 1) {
              filmVu.forEach(async (e, indexFilm) => {
                url += `&movielist=${e}`;
                if (indexFilm == filmVu.length - 1) {
                  this.movies = await movieService.getMovies(token, url, 50);
                }
              });
            }
          });
        }
      });
    },
  },
  component: {
    FilmDetails,
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
