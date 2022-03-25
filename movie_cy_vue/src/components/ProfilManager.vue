<template>
  <div class="donnees">
    <el-row :gutter="10">
      <el-col :xs="24" :sm="24" :md="24" :lg="12" :xl="24">
        <div class="username">
          {{ user.pseudo }}
          <el-avatar
            class="iconGroup"
            :style="{ backgroundColor: '#faa427' }"
            :size="100"
            :src="user.icon"
          />
        </div>
      </el-col>
    </el-row>

    <el-row :gutter="10">
      <el-col :xs="24" :sm="24" :md="24" :lg="12" :xl="12">
        <div class="username">
          <el-descriptions title="Vos informations">
            <el-descriptions-item label="Type de film favori n°1">
              {{ user.genre }}
            </el-descriptions-item>
            <el-descriptions-item label="Type de film favori n°2">
              {{ user.genreFlex }}
            </el-descriptions-item>
            <el-descriptions-item label="Acteur favori">
              {{ user.acteur }}
            </el-descriptions-item>
            <el-descriptions-item label="Réalisateur favori">
              {{ user.realisateur }}
            </el-descriptions-item>
            <el-descriptions-item label="Date de naissance">
              {{ user.ddn }}
            </el-descriptions-item>
          </el-descriptions>
        </div>
      </el-col>
    </el-row>
    <div style="display: flex">
      <el-button type="primary" class="btnValider"
        >Modifier ces informations</el-button
      >
    </div>
  </div>
</template>

<script lang="ts">
export default {
  data: function () {
    return {
      user: {
        id: 1,
        pseudo: "KAKASHIIIIIIIIIIIII",
        email: "a@a.fr",
        mdp: "ajdzfrezfez",
        films: "bla",
        groupes: ["groupe 1", "groupe 2", "groupe 3"],
        mood: "bien",
        acteur: "Tom Hanks",
        realisateur: "Clint Eastwood",
        genre: "Comédie",
        genreFlex: "Horreur",
        ddn: "19/08/98",
        icon: "/src/components/icon/CharacterIcon/captain-america.svg",
      },
    };
  },
};
</script>

<style lang="scss" scoped>
@import "../assets/constant.scss";

.el-descriptions__cell {
  width: 100%;
}

tr {
  display: flex;
  flex-wrap: wrap;
}

.username {
  font-size: 60px;
  display: flex;
}

.btnValider {
  background-color: $yellow;
  margin-right: 0px !important;
  border: none;
  border-radius: 20px;
  font-family: "Raleway", sans-serif;
  font-weight: bold;
  font-size: 20px;
}

.el-avatar {
  margin-left: 10%;
}

.el-descriptions__cell {
  font-size: 20px !important;
}

.el-descriptions__cell {
  width: 100%;
}

td {
  width: 100%;
}
</style>
