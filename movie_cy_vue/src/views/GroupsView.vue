<template>
  <div class="centerItems">
    <div class="accueil">
      <img src="../components/icon/utilIcon/logo.svg" />
      <span class="choose-group">Accédez à un de vos groupes</span>
      <div class="buttonGroup">
        <el-carousel
          :arrows="always"
          :interval="8000"
          type="card"
          height="200px"
        >
          <el-carousel-item v-for="item in this.groupes" :key="item">
            <span class="title-carousel-item">{{ item.nom }}</span>
            <el-avatar
              class="iconGroup avatar-profil"
              :style="{ backgroundColor: '#faa427' }"
              :size="130"
              :src="item.photo"
            />
          </el-carousel-item>
        </el-carousel>
      </div>
      <div class="go-create-group">
        <span>Ou créez en un</span>
        <router-link to="/groupCreation">
          <el-avatar :size="40" class="icon-add">
            <el-icon><plus /></el-icon
          ></el-avatar>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import RegisterForm from "../components/RegisterForm.vue";
import Connect from "../components/Connect.vue";
import { Plus } from "@element-plus/icons-vue";
import router from "../router/index";
import GroupsService from "../services/GroupsService";
import userService from "../services/userService";
const redirectCreateGroup = () => {
  router.push("/");
};
</script>

<script lang="ts">
export default {
  data() {
    return {
      groupes: [],
    };
  },
  methods: {
    async getUserGroups(user) {
      const token = JSON.parse(localStorage.getItem("user"));
      //On récupère les id des groupes de l'utilisateur
      const groupes_id = user.groupes;

      groupes_id.forEach(async (element) => {
        this.groupes.push(await GroupsService.getGroup(token, element));
      });
      console.log(this.groupes);
    },
  },
  async mounted() {
    const token = JSON.parse(localStorage.getItem("user"));
    let user = await userService.getUser(token);
    this.getUserGroups(user);
    console.log(this.groupes);
  },
};
</script>

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
  padding-top: 10%;
  padding-left: 10%;
  padding-right: 10%;
  padding-bottom: 7%;
}

.choose-group {
  padding-bottom: 5%;
  font-style: $font;
  font-size: 22px;
  color: white;
  font-weight: bold;
}

.go-create-group {
  padding-bottom: 10% !important;
  font-style: $font;
  font-size: 22px;
  color: white;
  font-weight: bold;
  display: contents;
}

.icon-add {
  margin-top: 5%;
  margin-bottom: 5%;
  background-color: $yellow;
  color: white;
  border: solid #d57e00;
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

.el-carousel {
  width: 300px;
}

.el-carousel__item h3 {
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
  text-align: center;
}

.el-carousel__item:nth-child(2n) {
}

.el-carousel__item:nth-child(2n + 1) {
}

.title-carousel-item {
  text-align: center;
  color: white;
}
</style>
<style>
.el-carousel__mask {
  background-color: transparent !important;
}
</style>
