<script setup>
/* eslint-disable vue/no-mutating-props */
import { InfoFilled } from "@element-plus/icons-vue";
</script>

<template>
  <div class="details">
    <el-button
      type="primary"
      title="Plus d'info"
      size="large"
      @click="show = true"
      :icon="InfoFilled"
      circle
    />
    <el-dialog
      custom-class="dialog dialog-detail"
      v-model="show"
      :title="movie.title"
    >
      <div class="entete-details">
        <div class="content-details">
          <div class="affiche-details">
            <img :src="movie.image" class="image-details" />
          </div>
          <div class="right">
            <div class="iconGenre-details">
              <div
                class="iconSpace-details"
                v-for="genre in movie.genreList"
                :key="genre"
              >
                <el-avatar
                  id="photoGroup"
                  :style="{ backgroundColor: '#faa427' }"
                  :size="large"
                  :title="genre.key"
                  :src="genre.value"
                />
              </div>
            </div>
            <div class="plot">
              {{ movie.plot }}
            </div>
            <div class="stars">Acteurs : {{ movie.stars }}</div>
            <div class="stars">Durée : {{ movie.runtimeStr }}</div>
          </div>
        </div>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  movie: Object,
  show: Boolean,
  props: ["movie", "show"],
};
</script>

<style lang="scss" scoped>
@import "../assets/constant.scss";

.content-details {
  margin-bottom: 5%;
}

.image-details {
  max-width: 60%;
}

.affiche-details {
  display: flex;
  justify-content: center;
}

.content-details {
  display: flex;
  flex-direction: row;
}

.iconGenre-details {
  display: flex;
  flex-direction: row;
}

.iconSpace-details {
  margin: 1px;
}

.plot {
  color: white;
  padding-top: 5%;
}

.stars {
  color: white;
  padding-top: 5%;
}

.icon-details {
  display: flex;
  justify-content: space-evenly;
  margin-top: 5%;
}

@media screen and (max-width: 1550px) and (min-width: 850px) {
  .image-details {
    max-width: 70%;
  }
}

@media screen and (max-width: 850px) {
  .affiche-details {
    visibility: hidden;
    width: 0%;
  }
}

@media screen and (max-width: 700px) {
  .el-dialog {
    width: 70%;
  }
}
</style>

<style lang="scss">
/** Utile pour FilmDetails.vue */
@import "../assets/constant.scss";

.dialog-detail {
  background-color: $gray !important;
  border-radius: 10px;
  height: initial !important;
}

.el-dialog__header {
  display: flex;
  font-weight: bold;
  margin-right: 0px !important;
}

.el-dialog__title {
  margin-left: auto;
  margin-right: auto;
  color: white;
}

@media screen and (max-width: 700px) {
  .el-dialog {
    width: 70%;
  }
}

.el-dialog__close {
  color: white !important;
}
</style>
