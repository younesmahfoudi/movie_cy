<script setup>
import RegisterForm from "../components/RegisterForm.vue";
import Connect from "../components/Connect.vue";
</script>

<template>
  <div class="centerItems">
    <div class="accueil">
      <img src="../components/icon/utilIcon/logoYellow.svg" />
      <div class="buttonGroup">
        <div :style="{ padding: '10px' }">
          <RegisterForm />
        </div>
        <div :style="{ padding: '10px' }">
          <Connect />
        </div>
      </div>
    </div>
    <router-view></router-view>
  </div>
</template>

<style lang="scss" scoped>
@import "../assets/constant.scss";

.centerItems {
  background-image: url("../components/icon/filmHome.jpg");
  background-size: cover;
  display: flex;
  justify-content: center;
  align-items: center;
  min-width: 100%;
  min-height: 100%;
}

.accueil {
  background-color: $darkGray;
  border-radius: $radius;
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  width: 30%;
}

.buttonGroup {
  display: flex;
  justify-content: center;
  flex-direction: row;
  padding-bottom: 5%;
}

#buttonHome {
  margin: 10%;
}

img {
  max-width: 50%;
  padding: 10%;
}

@media screen and (max-width: 1000px) and (min-width: 601px) {
  .accueil {
    width: 50% !important;
  }
}

@media screen and (max-width: 600px) {
  .accueil {
    width: 80% !important;
  }
}
</style>
