<template>
  <div>
    <div v-if="route.includes(`http://localhost:3000/movieGroupList`)">hey</div>
    <div class="button-list">
      <el-button
        v-if="route.includes(`http://localhost:3000/movieGroupList`)"
        type="warning"
        class="darkGray"
        @click="goProfil"
        round
        >Groupe :
      </el-button>

      <el-button
        v-if="this.canAccessToGroup"
        type="warning"
        class="darkGray"
        round
        @click="goGroupe()"
        >Groupe</el-button
      >

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
import authService from "../services/auth.service";
import router from "../router/index";

export default {
  props: {
    afficherBoutonProfil: Boolean,
  },
  data() {
    return {
      route: this.$route.params.toString(),
      groupe: {},
      canAccessToGroup: "",
    };
  },
  methods: {
    logout() {
      // authService.logout();
      this.$store.dispatch("auth/logout");
      this.$router.push("/");
    },

    goProfil() {
      router.push("/profil");
    },
    goGroupe() {
      router.push("/group?ref=" + this.$route.query.id);
    },
  },
  mounted() {
    this.canAccessToGroup = window.location
      .toString()
      .includes("movieGroupList");
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
