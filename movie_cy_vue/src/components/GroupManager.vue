<template>
  <div class="content">
    <div class="pdp">
      <el-avatar
        class="iconGroup avatar-profil"
        :style="{ backgroundColor: '#faa427' }"
        :size="170"
        :src="this.groupe.photo"
      />
    </div>
    <div class="names-bloc">
      <div class="names">
        <span>{{ groupe.nom }} </span>
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
            <span class="title-card">Informations du groupe</span>
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
            <el-col class="key" :span="12">Nom du groupe </el-col>
            <el-col :span="12">{{ groupe.nom }} </el-col>
          </el-row>
          <el-row>
            <el-col class="key" :span="12">Admin du groupe </el-col>
            <el-col :span="12">
              <div class="info-admin-groupe">
                <img :src="findSrcOfAvatarWithLabel('Avatar')" />
                <li class="li-membre">Nom admin</li>
              </div></el-col
            >
          </el-row>

          <el-row>
            <el-col class="key" :span="12">Membres du groupe </el-col>
            <el-col :span="12">
              <div class="info-membre-groupe">
                <span
                  style="display: flex; margin-bottom: 3%"
                  v-for="membre in groupe.membres_groupe"
                  :key="membre"
                >
                  <img :src="findSrcOfAvatarWithLabel(membre.avatar)" />
                  <li class="li-membre">
                    <span class="nom-membre">{{ membre.nom }} </span>
                  </li>
                </span>
              </div>
            </el-col>
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

      <span class="title"> Modification des informations du groupe</span>

      <div class="formulaire">
        <el-form
          label-position="top"
          ref="ruleFormRef"
          :rules="rules"
          :model="this.groupe"
        >
          <el-form-item label="Nom du groupe" prop="nom">
            <el-input
              input-style="font-family:'Raleway', sans-serif; font-weight: bold;"
              v-model="groupe.nom"
              placeholder="Nom"
            />
          </el-form-item>

          <el-form-item prop="avatar" label="Avatar du groupe">
            <el-select class="m-2" v-model="groupe.label" size="large">
              <div class="iconGrid">
                <el-option
                  v-for="item in iconForGroup"
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
              :size="70"
            >
              <img :src="findSrcOfGroupWithLabel(groupe.label)" />
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
  </div>
</template>

<script lang="ts">
import { ref, reactive } from "vue";
import { iconForGroup } from "./data/iconForGroup";
import { avatarForUser } from "./data/avatarForUser";
import { FormInstance } from "element-plus";
const dialogInfosPerso = ref(false);
const dialogInfosContenu = ref(false);
const ruleFormRef = ref<FormInstance>();

export default {
  data() {
    return {
      groupe: [],
      rules: reactive({
        nom: [{ validator: this.checkNom, trigger: "blur", required: true }],
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
    async getGroupMembres() {
      const token = JSON.parse(localStorage.getItem("user"));
      GroupsService.getGroup(token, this.user.id);
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
      const groupObject = iconForGroup.filter((group) => group.photo === src);
      return groupObject[0].label;
    },

    findSrcOfAvatarWithLabel(label) {
      const avatarObject = avatarForUser.filter(
        (avatar) => avatar.label === label
      );
      return avatarObject[0].photo;
    },

    findSrcOfGroupWithLabel(label) {
      const groupObject = iconForGroup.filter((group) => group.label === label);
      return groupObject[0].photo;
    },
    updateUser() {
      this.dialogInfosPerso = false;
      this.dialogInfosContenu = false;
    },
    async getInfosMembreGroupe() {
      const token = JSON.parse(localStorage.getItem("user"));

      for (let i = 0; i < this.groupe.membres.length; i++) {
        let user = await userService.getSpecificUser(
          token,
          this.groupe.membres[i]
        );
        this.groupe["membres_groupe"][i] = {
          nom: user.prenom + " " + user.nom,
          avatar: user.avatar,
        };
      }
    },
  },
  async mounted() {
    const token = JSON.parse(localStorage.getItem("user"));
    this.groupe = await GroupsService.getGroup(token, this.$route.query.ref);
    this.groupe["nom_membres"] = [];
    this.groupe["avatar_membres"] = [];
    this.getInfosMembreGroupe();
    this.groupe["membres_groupe"] = [];
  },
  computed: {
    isComplete() {
      return this.groupe.nom && this.groupe.label && this.groupe.membres;
    },
  },
};
</script>


<script lang="ts" setup>
import { Edit } from "@element-plus/icons-vue";
import GroupsService from "../services/GroupsService";
import userService from "../services/userService";
</script>

<style lang="scss" scoped>
@import "../assets/constant.scss";

.el-select {
  width: 100%;
}

.el-avatar {
  display: flex;
  margin-left: auto;
  margin-right: auto;
  margin-top: 5%;
}

.iconGrid {
  display: grid;
  grid-template-columns: auto auto auto;
}

.el-select-dropdown__item {
  height: 55px !important;
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

.li-membre {
  display: flex;
  justify-content: center;
  align-items: center;
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

.dialog-footer button:first-child {
  margin-right: 0px !important;
}

.info-admin-groupe {
  display: flex;
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
  text-align: center;
}

.names span {
  font-weight: bold;
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
</style>