<template>
<<<<<<< HEAD
  <div id="profil">   
    <div class="common-layout">
        <el-container>
        <el-container>
            <el-header>  
            <div id="header-monprofil">
                <div> USERNAME  </div>  
                <div> <el-avatar :size="50" :src="circleUrl" />
                </div>
            </div>
            </el-header>
            <el-main>
                <div>
                    <ul>
                        <li> Mon type préféré: </li>
                        <li> Mon second type préféré: </li>
                        <li> Mon acteur preferé: </li>
                        <li> Mon réalisateur preferé: </li>
                    </ul>       
                </div>
                <el-button type="warning">Modifier</el-button>
            </el-main>
        </el-container>
        </el-container>
    </div>
  </div> 
</template>

<style>
#header-monprofil{
    display: flex;
    justify-content: space-between;
    width: 100%;
}
#profil{
    display: block;
    width: 400px;
}

#profil ul {
        list-style: none;
}

</style>
=======
  <div class="donnees">
    <div class="entete">
      <div class="entete-content">
        <div class="username">
          {{ user.pseudo }}
          <div class="nom">
            {{ user.prenom }}
            {{ user.nom }}
          </div>
        </div>
        <div class="pdp">
          <el-avatar
            class="iconGroup"
            :style="{ backgroundColor: '#faa427' }"
            :size="200"
            :src="user.icon"
          />
        </div>
      </div>
    </div>
    <div class="information">
      Vos informations
      <div class="user-info">
        <div class="row">
          <div>Type de film favori n°1</div>
          <div>{{ user.genre }}</div>
        </div>
        <div class="row">
          <div>Type de film favori n°2</div>
          <div>{{ user.genreFlex }}</div>
        </div>
        <div class="row">
          <div>Acteur favori</div>
          <div>{{ user.acteur }}</div>
        </div>
        <div class="row">
          <div>Réalisateur favori</div>
          <div>{{ user.realisateur }}</div>
        </div>
        <div class="row">
          <div>Date de naissance</div>
          <div>{{ user.ddn }}</div>
        </div>
      </div>
    </div>
    <div style="float: right; margin-right: 10%; margin-top: 2%">
      <el-button type="warning" class="btnValider" round>
        Modifier ces informations
      </el-button>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      user: {
        id: 1,
        pseudo: "Mahfoudiyodiyo",
        prenom: "younes",
        nom: "la pute",
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
        icon: "/src/components/icon/CharacterIcon/avatar.svg"
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
  font-size: 50px;
  display: flex;
  flex-direction: column;
}

.nom {
  font-size: 20px;
}

.entete {
  display: flex;
  flex-direction: row;
  justify-content: center;
  width: 100%;
}

.entete-content {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 80%;
}

.information {
  display: flex;
  flex-direction: column;
  justify-content: center;
  font-size: 40px;
  align-items: center;
}

.user-info {
  display: flex;
  flex-direction: column;
  font-size: 20px;
  width: 80%;
}

.row {
  display: flex;
  justify-content: space-between;
}

@media screen and (max-width: 700px) {
  .entete-content {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .username{
    display: flex;
    align-items: center;
    font-size: 20px;
  }

  .nom {
    font-size: 15px;
  }

  .pdp{
    order:1;
  }

  .information {
    font-size: 20px;
    margin-top: 5%;
  }

  .user-info {
    margin-top: 5%;
    font-size: 15px;
  }
}
</style>
>>>>>>> efd0783ce845f7d992372ac92097879970ae1318
