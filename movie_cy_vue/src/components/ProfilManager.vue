<template>
  <div class="content">
    <div class="pdp">
      <el-avatar
        class="iconGroup avatar-profil"
        :style="{ backgroundColor: '#faa427' }"
        :size="170"
        :src="this.avatar_src"
       
      />
    </div>
    <div class="names-bloc">
      <div class="names">
        <span style="margin-right: 5%">{{ user.prenom }} </span>
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
              @click="dialogInfosContenu = true"
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
        </el-card>
      </el-col>
    </el-row>

    <el-dialog
      custom-class="dialog"
      v-model="dialogInfosPerso"
      width="35%"
      :close-on-click-modal="false"
      :show-close="false"
      :close-on-press-escape="false"
    >
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
          :model="this.user"
        >
          <div class="names">
            <el-form-item
              label="Prénom"
              prop="prenom"
              style="width: 47%; margin-right: 6%"
            >
              <el-input
                input-style="font-family:'Raleway', sans-serif; font-weight: bold;"
                v-model="user.prenom"
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
              input-style="font-family:'Raleway', sans-serif; font-weight: bold;"
              name="password"
              v-model="user.mdp"
              type="password"
              placeholder="Mot de passe"
              show-password
              autocomplete="off"
            />
          </el-form-item>

          <el-form-item prop="checkMdpInput" label="Confirmation mot de passe">
            <el-input
              input-style="font-family:'Raleway', sans-serif; font-weight: bold;"
              name="password1"
              v-model="user.checkMdpInput"
              type="password1"
              placeholder="Mot de passe"
              show-password
              autocomplete="off"
            />
          </el-form-item>

          <el-form-item prop="avatar" label="Avatar">
            <el-select class="m-2" v-model="user.icon" size="large">
              <div class="iconGrid">
                <el-option
                  v-for="item in avatarForUser"
                  :key="item.value"
                  :value="item.label"
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
              <!-- <img :src="findSrcOfAvatarWithLabel(user.avatar)" /> -->
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
              @click="updateUser()"
              round
              :disabled="!isComplete"
            >
              Valider
            </el-button>
          </span>
        </div>
      </template>
    </el-dialog>

    <el-dialog
      custom-class="dialog"
      v-model="dialogInfosContenu"
      width="35%"
      :close-on-click-modal="false"
      :show-close="false"
      :close-on-press-escape="false"
    >
      <img
        class="imgForm"
        :style="{ maxWidth: '30%' }"
        src="/src/components/icon/utilIcon/logo.svg"
      />

      <span class="title"> Modification de votre contenu préféré</span>

      <div class="formulaire">
        <el-form
          label-position="top"
          ref="ruleFormRef"
          :rules="rules"
          :model="this.user"
        >
          <el-row :gutter="10" style="display: flex">
            <el-col
              class="responsive-card"
              :xs="24"
              :sm="24"
              :md="24"
              :lg="12"
              :xl="12"
            >
              <el-form-item label="Type de film favori n°1" prop="type1">
                <el-select
                  v-model="user.genre"
                  class="m-2 contenu-fav"
                  placeholder="Select"
                  size="large"
                >
                  <el-option
                    v-for="item in listeGenres"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                  />
                </el-select>
              </el-form-item>
            </el-col>

            <el-col
              class="responsive-card"
              :xs="24"
              :sm="24"
              :md="24"
              :lg="12"
              :xl="12"
            >
              <el-form-item label="Type de film favori n°2" prop="type2">
                <el-select
                  v-model="user.genreFlex"
                  class="m-2 contenu-fav"
                  placeholder="Select"
                  size="large"
                >
                  <el-option
                    v-for="item in listeGenres"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                  />
                </el-select>
              </el-form-item>
            </el-col>
          </el-row>

          <el-row :gutter="10" style="display: flex">
            <el-col
              class="responsive-card"
              :xs="24"
              :sm="24"
              :md="24"
              :lg="12"
              :xl="12"
            >
              <el-form-item label="Acteur favori" prop="acteur">
                <el-select
                  v-model="user.acteur"
                  filterable
                  allow-create
                  default-first-option
                  :reserve-keyword="false"
                  placeholder="Acteur favori"
                  class="m-2 contenu-fav"
                >
                  <el-option
                    v-for="item in listeActeurs"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                  />
                </el-select>
              </el-form-item>
            </el-col>

            <el-col
              class="responsive-card"
              :xs="24"
              :sm="24"
              :md="24"
              :lg="12"
              :xl="12"
            >
              <el-form-item label="Réalisateur favori" prop="type1">
                <el-select
                  v-model="user.realisateur"
                  filterable
                  allow-create
                  default-first-option
                  :reserve-keyword="false"
                  placeholder="Réalisateur favori"
                  class="m-2 contenu-fav"
                >
                  <el-option
                    v-for="item in listeRealisateurs"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                  />
                </el-select>
              </el-form-item>
            </el-col>
          </el-row>
        </el-form>
      </div>

      <template #footer>
        <div style="display: flex">
          <span class="dialog-footer">
            <el-button
              class="validate"
              type="warning"
              @click="updateUser()"
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
import { ref, reactive } from "vue";
import { avatarForUser } from "./data/avatarForUser";
import { listeGenres } from "./data/listeGenres";
import { listeActeurs } from "./data/listeActeurs";
import { listeRealisateurs } from "./data/listeRealisateurs";
import { FormInstance } from "element-plus";
const dialogInfosPerso = ref(false);
const dialogInfosContenu = ref(false);
const ruleFormRef = ref<FormInstance>();

export default {
  data() {
    return {
      user: {
      },
      label:'',
      avatar_src:'',

      rules: reactive({
        prenom: [
          { validator: this.checkPrenom, trigger: "blur", required: true },
        ],
        nom: [{ validator: this.checkNom, trigger: "blur", required: true }],
        email: [
          {
            required: true,
            message: "Veuillez saisir une adresse email.",
            trigger: "blur",
          },
          {
            type: "email",
            message: "Veuillez saisir une adresse email correcte.",
            trigger: ["blur", "change"],
          },
        ],
        ddn: [{ validator: this.checkAge, trigger: "blur", required: true }],
        mdp: [
          { validator: this.validatePass, trigger: "blur", required: true },
        ],
        checkMdpInput: [
          { validator: this.validatePass2, trigger: "blur", required: true },
        ],
        avatar: [
          { validator: this.checkAvatar, trigger: "blur", required: true },
        ],
      }),
    };
  },
  methods: {
    changeImg(e) {
      this.user.icon = this.findLabelOfAvatarWithSrc(e);
    },
    getGroupes(groupes) { 
      // if (groupes !== undefined || groupes !== [] || groupes !== null){
      // return groupes.map((groupe) => {
      //   return "<li>" + groupe + "</li>";
      // });
      // }
    },
    validatePass(rule, value, callback) {
      if (value === "") {
        callback(new Error("Veuillez saisir un mot de passe"));
      } else {
        if (value !== "") {
          if (value.length < 6 || !/\d/.test(value)) {
            callback(
              new Error(
                "Votre mot de passe doit être composé d'au moins 6 caractères et d'au moins un chiffre"
              )
            );
          }
          if (!this.ruleFormRef.value) return;
          this.ruleFormRef.value.validateField("checkPass", () => null);
        }
        callback();
      }
    },
    validatePass2(rule, value, callback) {
      if (value === "") {
        callback(new Error("Réessayez"));
      } else if (value !== this.user.mdp) {
        callback(new Error("Les mots de passe sont différents"));
      } else {
        callback();
      }
    },
    calculateAgeFromDate(birthday) {
      var ageDifMs = Date.now() - birthday.getTime();
      var ageDate = new Date(ageDifMs);
      return Math.abs(ageDate.getUTCFullYear() - 1970);
    },
    isDateBeforeToday(date) {
      if (date) {
        return (
          new Date(date.toDateString()) < new Date(new Date().toDateString())
        );
      }
    },
    checkAge(rule, value, callback) {
      setTimeout(() => {
        if (!value) {
          callback(new Error("Veuillez choisir une date."));
        }
        if (!this.isDateBeforeToday(value)) {
          callback(
            new Error("Veuillez choisir une date de naissance correcte.")
          );
        } else {
          if (this.calculateAgeFromDate(value) < 18) {
            callback(new Error("Vous devez avoir plus de 18 ans."));
          } else {
            callback();
          }
        }
      }, 1000);
    },
    checkPrenom(rule, value, callback) {
      if (!value || value === "") {
        callback(new Error("Veuillez saisir un prénom."));
      }
    },
    checkNom(rule, value, callback) {
      if (!value || value === "") {
        callback(new Error("Veuillez saisir un nom."));
      }
    },
    checkAvatar(rule, value, callback) {
      if (!value || value === "") {
        callback(new Error("Veuillez choisir un avatar."));
      }
    },
    findLabelOfAvatarWithSrc(src) {
      if (src.substring(0, 1) !== ".") {
        src = "." + src;
      }
      const avatarObject = avatarForUser.filter(
        (avatar) => avatar.photo === src
      );
      return avatarObject[0].label;
    },

    async findSrcOfAvatarWithLabel() {
      const avatarObject = avatarForUser.filter(
        (avatar) => avatar["label"] === this.label
      );
      this.avatar_src = avatarObject[0].photo;
    },
    updateUser() {
      this.dialogInfosPerso = false;
      this.dialogInfosContenu = false;
    },
  },
  computed: {
    isComplete() {
      return (
        this.user.prenom &&
        this.user.nom &&
        this.user.ddn &&
        this.user.email &&
        this.user.mdp &&
        this.user.checkMdpInput &&
        this.user.icon
      );
    },
  },
  async mounted() {
    const token = JSON.parse(localStorage.getItem("user"));
    this.user = await userService.getUser(token);
    this.label = this.user.avatar;
    this.findSrcOfAvatarWithLabel();
  }
};
</script>


<script lang="ts" setup>
import { Edit } from "@element-plus/icons-vue";
import userService from '../services/userService';
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

.contenu-fav {
  width: 100%;
}
</style>


<style>
.typesPref {
  display: flex;
}

.staffPref {
  display: flex;
}
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
