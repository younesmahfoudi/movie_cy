<template>
  <div class="content">
    <div class="pdp">
      <el-avatar
        class="iconGroup avatar-profil"
        :style="{ backgroundColor: '#faa427' }"
        :size="170"
        :src="this.findSrcOfGroupWithLabel(group.label)"
      />
    </div>
    <div class="names-bloc">
      <div class="names">
        <span>{{ group.nom }} </span>
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
            <el-col :span="12">{{ group.nom }} </el-col>
          </el-row>

          <el-row>
            <el-col class="key" :span="12">Membres du groupe </el-col>
            <el-col :span="12" v-html="getMembres(group.membres)"> </el-col>
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
          :model="this.group"
        >
          <el-form-item label="Nomdu groupe" prop="nom">
            <el-input
              input-style="font-family:'Raleway', sans-serif; font-weight: bold;"
              v-model="group.nom"
              placeholder="Nom"
            />
          </el-form-item>

          <el-form-item prop="avatar" label="Avatar du groupe">
            <el-select class="m-2" v-model="group.label" size="large">
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
              <img :src="findSrcOfGroupWithLabel(group.label)" />
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
      group: {
        id: 1,
        nom: "Groupe ICC",
        label: "Espion",
        membres: [
          {
            prenom: "Younes",
            nom: "Mahfoudi",
            email: "aaa@aaa.fr",
            label: "Avatar",
          },
          {
            prenom: "Etienne",
            nom: "Tournier",
            email: "aaa@aaa.fr",
            label: "Kakashi",
          },
          {
            prenom: "Tom",
            nom: "Soulage",
            email: "aaa@aaa.fr",
            label: "Avatar",
          },
        ],
      },
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
    getMembres(membres) {
      return membres.map((membre) => {
        const imgMembre = this.findSrcOfAvatarWithLabel(membre.label);
        return (
          "<li><el-avatar> <img src=" +
          imgMembre +
          " /> </el-avatar>" +
          "<span class='info-membre'>"+
          membre.prenom +
          " " +
          membre.nom +
          " </span></li>"
        );
      });
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
  },
  computed: {
    isComplete() {
      return this.group.nom && this.group.label && this.group.membres;
    },
  },
};
</script>


<script lang="ts" setup>
import { Edit } from "@element-plus/icons-vue";
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