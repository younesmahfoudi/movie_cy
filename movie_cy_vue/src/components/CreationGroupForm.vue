<template>
  <div>
    <el-dialog
      custom-class="dialog"
      v-model="dialogGroupCreation"
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

      <span class="title"> Création d'un groupe</span>

      <div class="formulaire">
        <el-form
          :model="ruleForm"
          label-position="top"
          :rules="rules"
          label-width="120px"
        >
          <el-form-item prop="nom" label="Nom du groupe">
            <el-input v-model="ruleForm.nom" />
          </el-form-item>

          <el-form-item
            prop="photo"
            label="Image du groupe"
            class="input-image-groupe"
          >
            <el-select
              @change="(e) => changeImg(e)"
              v-model="ruleForm.photo"
              class="m-2"
              placeholder="Choisir une image de groupe"
              size="large"
            >
              <div class="iconGrid">
                <el-option
                  v-for="item in iconForGroup"
                  :key="item.value"
                  :value="item.photo"
                  :label="item.label"
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
              <img :src="imageSrc" />
            </el-avatar>
          </el-form-item>

          <el-form-item prop="membres" label="Membres du groupe">
            <el-input
              v-model="string_entered"
              placeholder="Chercher des utilisateurs (par le nom, prénom ou email )"
            />

            <div class="div-add-and-research-user">
              <el-card class="box-card">
                <div v-if="this.request_not_null">
                  <div
                    v-for="user in this.tab_users_list"
                    :key="user"
                    class="text item"
                  >
                    <div>
                      <el-button
                        type="primary"
                        @click="addToMembersList(user)"
                        round
                        >+</el-button
                      >
                      {{
                        user.prenom + " " + user.nom + " ( " + user.email + " )"
                      }}
                    </div>
                  </div>
                </div>
                <div v-if="!this.request_not_null">
                  <span> Aucun utilisateur trouvé</span>
                </div>
              </el-card>

              <el-card class="box-card">
                <template #header>
                  <div class="card-header">
                    <span>Membres du groupe</span>
                  </div>
                </template>
                <div
                  v-for="(user, index) in this.tab_members_list"
                  :key="user"
                  class="text item"
                >
                  <div v-if="index == 0">
                    Admin :
                    {{
                      user.prenom + " " + user.nom + " ( " + user.email + " )"
                    }}
                  </div>
                  <div v-if="index != 0">
                    <el-button
                      type="danger"
                      @click="removeToMembersList(user)"
                      round
                      >-</el-button
                    >
                    {{
                      user.prenom + " " + user.nom + " ( " + user.email + " )"
                    }}
                  </div>
                </div>
              </el-card>
            </div>
          </el-form-item>
        </el-form>
      </div>

      <template #footer>
        <div style="display: flex">
          <span class="dialog-footer">
            <el-button
              class="validate"
              type="warning"
              @click="createGroup()"
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
import GroupsService from "../services/GroupsService.js";
import axios from "axios";
import UserService from "../services/userService.js";
const dialogGroupCreation = ref(true);

export default {
  data() {
    return {
      imageSrc: "./src/components/icon/ThemeIcon/action.png",
      defaultLabel: "Pistolet",
      listImages: [],
      users_find: [],
      tab_users_list: [],
      tab_members_list: [],
      tab_id_members: [],
      string_entered: "",
      request_not_null: false,
    };
  },
  async mounted() {
    const token = JSON.parse(localStorage.getItem("user"));
    let user = await userService.getUser(token);
    this.tab_members_list.push(user);
    this.tab_id_members.push(user["id"]);
  },
  watch: {
    string_entered: function (value) {
      this.searchUser(value);
    },
  },
  methods: {
    changeImg(e) {
      this.imageSrc = e;
    },
    async createGroup() {
      const token = JSON.parse(localStorage.getItem("user"));
      this.ruleForm.membres = this.tab_id_members;
      this.ruleForm.admin = this.tab_id_members[0];
      console.log(this.ruleForm);

      const new_groupe = await GroupsService.createGroup(token, this.ruleForm);
      this.tab_members_list.map((element) => {
        element["groupes"].push(new_groupe.data.data[0]["id"]);
        UserService.updateUser(token, JSON.parse(JSON.stringify(element)));
      });
      router.push("/group?ref="+new_groupe.data.data[0].id);
    },
    async searchUser(string_entered) {
      const token = JSON.parse(localStorage.getItem("user"));

      const users = await UserService.getUsersWithStringEntered(
        token,
        string_entered
      );

      if (users != undefined && users.code != 200) {
        // On enlève l'admin du résultat de recherches d'utilisateurs
        this.users_find = users.filter(
          (user) => user["id"] != this.tab_id_members[0]
        );

        if (
          this.users_find.length != 0 &&
          string_entered != "" &&
          string_entered[0] != " "
        ) {
          //On enlève tous les utilisateurs ajoutés dans le tableau membre du résultat de recherches d'utilisateurs
          this.users_find.map((element1) => {
            this.tab_members_list.map((element2) => {
              if (element1["id"] == element2["id"]) {
                this.users_find.splice(this.users_find.indexOf(element1), 1);
              }
            });
          });

          this.tab_users_list = this.users_find;

          if (this.tab_users_list.length != 0) {
            this.request_not_null = true;
          }
        } else {
          this.request_not_null = false;
        }
      }
    },
    arrayRemove(arr, value) {
      return arr.filter(function (ele) {
        return ele != value;
      });
    },
    addToMembersList(user) {
      this.tab_members_list.push(user);
      this.tab_id_members.push(user["id"]);
      this.tab_users_list = this.arrayRemove(this.tab_users_list, user);
    },
    removeToMembersList(user) {
      this.tab_users_list.push(user);
      this.tab_id_members = this.arrayRemove(this.tab_id_members, user["id"]);
      this.tab_members_list = this.arrayRemove(this.tab_members_list, user);
    },
    updateGroupsUser(user) {
      UserService.updateUser(JSON.parse(localStorage.getItem("user")), user);
    },
  },
  computed: {
    isComplete() {
      return this.ruleForm.nom;
    },
  },
};
</script>
  
  <script lang="ts" setup>
import { iconForGroup } from "./data/iconForGroup";
import userService from "../services/userService.js";
import router from '../router/index.js';

const ruleForm = reactive({
  nom: "",
  photo: "",
  membres: "", // A CHANGER AVEC ID DU MEC CONNECTE + LES AUTRES USERS
  admin: "", // A CHANGER AVEC ID DU MEC CONNECTE
});

const checkNom = (rule: any, value: any, callback: any) => {
  if (!value || value === "") {
    callback(new Error("Veuillez saisir un nom de groupe"));
  }
};

const checkPhoto = (rule: any, value: any, callback: any) => {
  if (!value || value === "") {
    callback(new Error("Veuillez choisir une photo."));
  }
};

const rules = reactive({
  nom: [{ validator: checkNom, trigger: "blur", required: true }],
  photo: [{ validator: checkPhoto, trigger: "blur", required: true }],
});

const value = ref("");
</script>
  
  <style lang="css" scoped>
.el-select {
  width: 100% !important;
}
.iconGroup {
  margin-left: auto;
  margin-right: auto;
  display: block;
}
.el-avatar {
  margin-left: 5%;
}
.el-select-dropdown__item {
  height: 55px !important;
}

.iconGrid {
  display: grid;
  grid-template-columns: auto auto auto auto auto;
}

.oneGroup {
  padding-top: 5px;
}

.avatarHidden {
  visibility: hidden;
}

.avatarVisible {
  visibility: visible;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.box-card {
  width: 480px;
}

.div-add-and-research-user {
  display: flex;
}

.div-add-and-research-user {
  display: block;
}

.div-add-and-research-user {
  width: 100%;
}

.box-card {
  width: 100%;
}

.el-avatar {
  margin-left: auto !important;
  margin-right: auto !important;
  margin-top: 2%;
}

.input-image-groupe {
  margin-bottom: 4% !important;
}

.el-card__header {
  padding-top: 0px !important;
  padding-bottom: 0px !important;
}

.el-card {
  margin-bottom: 5%;
}

.card-header {
  margin-left: auto;
  margin-right: auto;
}
</style>

<style >
.el-card__header {
  padding-top: 0px !important;
  padding-bottom: 0px !important;
  display: flex;
}
</style>
