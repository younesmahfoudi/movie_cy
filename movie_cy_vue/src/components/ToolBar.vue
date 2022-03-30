<template>
  <div>
    <div v-if="route.includes(`http://localhost:3000/movieGroupList`)">hey</div>
    <div class="button-list">
      <el-button type="warning" class="darkGray" @click="goProfil" round
        >Profil</el-button
      >

      <el-button type="warning" class="darkGray" @click="logout" round
        >Déconnexion</el-button
      >
    </div>
  </div>
</template>

<script lang="ts">
import authService from "../services/authService";
import router from "../router/index";

export default {
  data() {
    return {
      route: this.$route.params.toString(),
      groupe: {},
    };
  },
  methods: {
    logout() {
      authService.logout();
    },

    goProfil() {
      router.push("/profil");
    },
  },
};
</script>

<style lang="scss">
@import "../assets/constant.scss";

.button-list {
  float: right;
}

.darkGray {
  margin: 10px;
}
</style>
