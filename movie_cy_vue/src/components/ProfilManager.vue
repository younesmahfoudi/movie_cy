<template>
  <div class="content">
    <div class="pdp">
      <el-avatar
        class="iconGroup avatar-profil"
        :style="{ backgroundColor: '#faa427' }"
        :size="170"
        :src="user.icon"
      />
    </div>
    <div class="names-bloc">
      <div class="names">
        <span>{{ user.prenom }} </span>
        {{ user.nom }}
      </div>
    </div>

    <el-row :gutter="12" style="display: grid">
      <el-col
        class="responsive-card"
        :xs="24"
        :sm="24"
        :md="24"
        :lg="24"
        :xl="24"
      >
        <el-card shadow="always">
          <div class="card-header">
            <span class="title-card">Informations personnelles</span>
            <el-button
              type="primary"
              class="btn-modifier"
              :icon="Edit"
              circle
              @click="dialogInfosPerso = true"
            />
          </div>
          <hr class="ligne" />
          <el-row>
            <el-col class="key" :span="12">Prénom </el-col>
            <el-col :span="12">{{ user.prenom }} </el-col>
          </el-row>

          <el-row>
            <el-col class="key" :span="12">Nom </el-col>
            <el-col :span="12">{{ user.nom }} </el-col>
          </el-row>
          <el-row>
            <el-col class="key" :span="12">Adresse email </el-col>
            <el-col :span="12">{{ user.email }} </el-col>
          </el-row>

          <el-row>
            <el-col class="key" :span="12">Date de naissance </el-col>
            <el-col :span="12">{{ user.ddn }} </el-col>
          </el-row>
          <el-row>
            <el-col class="key" :span="12"> Groupes </el-col>
            <el-col :span="12" v-html="getGroupes(user.groupes)"> </el-col>
          </el-row>
        </el-card>
      </el-col>
      <el-col
        class="responsive-card"
        :xs="24"
        :sm="24"
        :md="24"
        :lg="24"
        :xl="24"
      >
        <el-card shadow="hover">
          <div class="card-header">
            <span class="title-card"
              >Informations sur votre contenu préféré</span
            >
            <el-button
              type="primary"
              class="btn-modifier"
              :icon="Edit"
              circle
            />
          </div>
          <hr class="ligne" />
          <el-row>
            <el-col class="key" :span="12">Type de film favori n°1 </el-col>
            <el-col :span="12">{{ user.genre }} </el-col>
          </el-row>

          <el-row>
            <el-col class="key" :span="12">Type de film favori n°2 </el-col>
            <el-col :span="12">{{ user.genreFlex }} </el-col>
          </el-row>
          <el-row>
            <el-col class="key" :span="12">Acteur favori </el-col>
            <el-col :span="12">{{ user.acteur }} </el-col>
          </el-row>
          <el-row>
            <el-col class="key" :span="12">Réalisateur favori </el-col>
            <el-col :span="12">{{ user.acteur }} </el-col>
          </el-row>
          <el-row>
            <el-col class="key" :span="12">Acteur favori </el-col>
            <el-col :span="12">{{ user.acteur }} </el-col>
          </el-row>
        </el-card>
      </el-col>
    </el-row>

    <el-dialog custom-class="dialog" v-model="dialogInfosPerso" width="35%">
      <img
        class="imgForm"
        :style="{ maxWidth: '30%' }"
        src="/src/components/icon/utilIcon/logo.svg"
      />

      <span class="title"> Modification de vos informations personnelles</span>

      <div class="formulaire">
        <el-form
          label-position="top"
          ref="ruleFormRef"
          :rules="rules"
        >
          <div class="names">
            <el-form-item
              label="Prénom"
              prop="prenom"
              style="width: 47%; margin-right: 6%"
            >
              <el-input
                input-style="font-family:'Raleway', sans-serif; font-weight: bold;"
                v-model="ruleForm.prenom"
                placeholder="Prénom"
                name="user.prenom"
              />
            </el-form-item>

            <el-form-item label="Nom" prop="nom" style="width: 47%">
              <el-input
                input-style="font-family:'Raleway', sans-serif; font-weight: bold;"
                v-model="user.nom"
                placeholder="Nom"
              />
            </el-form-item>
          </div>

          <el-form-item label="Date de naissance" prop="ddn">
            <el-date-picker
              v-model="user.ddn"
              type="date"
              placeholder="Date de naissance"
              style="width: 100%"
            />
          </el-form-item>
          <el-form-item prop="email" label="Adresse email">
            <el-input
              input-style="font-family:'Raleway', sans-serif; font-weight: bold;"
              name="email"
              v-model="user.email"
              placeholder="Adresse email"
            />
          </el-form-item>

          <el-form-item prop="mdp" label="Mot de passe">
            <el-input
              v-model="user.mdp"
              input-style="font-family:'Raleway', sans-serif; font-weight: bold;"
              name="password"
              type="password"
              placeholder="Mot de passe"
              show-password
              autocomplete="off"
            />
          </el-form-item>

          <el-form-item prop="checkPass" label="Confirmation mot de passe">
            <el-input
              input-style="font-family:'Raleway', sans-serif; font-weight: bold;"
              v-model="user.mdp"
              name="password"
              type="password"
              placeholder="Mot de passe"
              show-password
              autocomplete="off"
            />
          </el-form-item>
          <el-form-item prop="avatar" label="Avatar">
            <el-select
              class="m-2"
              :placeholder="defaultLabel"
              size="large"
            >
              <div class="iconGrid">
                <el-option
                  v-for="item in avatarForUser"
                  :key="item.value"
                  :value="item.photo"
                  :label="item.label"
                  @click="changeImg(item.photo)"
                >
                  <div class="oneGroup">
                    <el-avatar
                      class="iconGroup"
                      :style="{ backgroundColor: '#faa427' }"
                      :size="48"
                      :src="item.photo"
                    />
                  </div>
                </el-option>
              </div>
            </el-select>
            <el-avatar
              v-if="imageSrc !== ''"
              class="iconGroup"
              id="iconChoosenForChange"
              :style="{ backgroundColor: '#faa427' }"
              :size="50"
            >
              <img :src=user.icon />
            </el-avatar>
          </el-form-item>
        </el-form>
      </div>

      <template #footer>
        <div style="display: flex">
          <span class="dialog-footer">
            <el-button
              class="validate"
              type="warning"
              @click="createUser()"
              round
              :disabled="!isComplete"
            >
              Valider
            </el-button>
          </span>
        </div>
      </template>
    </el-dialog>
  </div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      user: {
        id: 1,
        prenom: "Younes",
        nom: "Mahfoudi",
        email: "mahfoudiyo@cy-tech.fr",
        mdp: "bite",
        films: "bla",
        groupes: ["Groupe 1", "Groupe 2", "Groupe 3"],
        mood: "bien",
        acteur: "Tom Hanks",
        realisateur: "Clint Eastwood",
        genre: "Comédie",
        genreFlex: "Horreur",
        ddn: "19/08/98",
        icon: "/src/components/icon/CharacterIcon/avatar.svg",
        defaultLabel: "Avatar",
        listImages: [],
      },
    };
  },
  methods: {
    changeImg(e) {
      this.user.icon = e;
    },
    getGroupes(groupes) {
      return groupes.map((groupe) => {
        return "<li>" + groupe + "</li>";
      });
    },
  },
};
</script>

<script lang="ts" setup>
import { ref, reactive } from "vue";
import { Edit } from "@element-plus/icons-vue";
import { avatarForUser } from "./data/avatarForUser";
const dialogInfosPerso = ref(false);

const checkPrenom = (rule: any, value: any, callback: any) => {
  console.log(value)
  if (!value || value === "") {
    callback(new Error("Veuillez saisir un prénom."));
  }
};

const ruleForm = reactive({
  prenom: "",
  nom: "",
  email: "",
  ddn: "",
  mdp: "",
  checkPass: "",
  avatar: "",
});


const rules = reactive({
  prenom: [{ validator: checkPrenom, trigger: "blur", required: true }]
  // nom: [{ validator: checkNom, trigger: "blur", required: true }],
  // email: [
  //   {
  //     required: true,
  //     message: "Veuillez saisir une adresse email.",
  //     trigger: "blur",
  //   },
  //   {
  //     type: "email",
  //     message: "Veuillez saisir une adresse email correcte.",
  //     trigger: ["blur", "change"],
  //   },
  // ],
  // ddn: [{ validator: checkAge, trigger: "blur", required: true }],
  // mdp: [{ validator: validatePass, trigger: "blur", required: true }],
  // checkPass: [{ validator: validatePass2, trigger: "blur", required: true }],
  // avatar: [{ validator: checkAvatar, trigger: "blur", required: true }],
});
</script>

<style lang="scss" scoped>
@import "../assets/constant.scss";

.iconGrid {
  display: grid;
  grid-template-columns: auto auto auto;
}

.el-select-dropdown__item {
  height: 55px !important;
}

.names {
  display: flex;
}
.avatar-profil {
  margin-left: auto;
  margin-right: auto;
}

.title-card {
  margin-left: auto;
  margin-right: auto;
}
.key {
  font-weight: bold;
  margin-bottom: 15px;
}

.el-col {
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 20px;
}

.ligne {
  border: 1px solid $yellow;
  border-radius: 20px;
}
.btn-modifier {
  background-color: $yellow;
  border-color: $yellow;
}
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

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
}

@media screen and (min-width: 650px) {
  .responsive-card {
    width: 70%;
  }
}

.username {
  display: flex;
  align-items: center;
  font-size: 20px;
}

.information {
  font-size: 20px;
  margin-top: 5%;
}

.user-info {
  margin-top: 5%;
  font-size: 15px;
}
</style>

<style>
.user-infos {
  background-color: grey;
  border-radius: 20px;
  font-size: 22px;
}
.pdp {
  display: flex !important;
  width: 100%;
}

.names-bloc {
  display: flex;
}
.names {
  margin-left: auto;
  margin-right: auto;
  font-size: 25px;
  margin-top: 10px;
  margin-bottom: 10px;
}

.names span {
  font-weight: bold;
}
</style>