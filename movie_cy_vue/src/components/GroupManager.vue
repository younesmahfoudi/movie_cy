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
              v-if="this.estAdmin(this.user_connecte, this.groupe)"
              type="primary"
              class="btn-modifier"
              :icon="Edit"
              circle
              @click="dialogInfosGroupe = true"
            />
          </div>
          <hr class="ligne" />
          <el-row>
            <el-col class="key" :span="12">Nom du groupe </el-col>
            <el-col :span="12">{{ groupe.nom }} </el-col>
          </el-row>

          <el-row>
            <el-col class="key" :span="12">Membres du groupe </el-col>
            <el-col :span="12">
              <div class="info-membre-groupe">
                <span
                  style="display: flex; margin-bottom: 3%"
                  v-for="(membre, index) in groupe.membres_groupe"
                  :key="membre"
                >
                  <div class="admin-li" v-if="index == 0">
                    <el-icon :size="50"><flag /></el-icon>
                    <img :src="findSrcOfAvatarWithLabel(membre.avatar)" />
                    <li class="li-membre">
                      <span class="nom-membre">{{ membre.nom }} (Admin) </span>
                    </li>
                  </div>

                  <img
                    v-if="index != 0"
                    :src="findSrcOfAvatarWithLabel(membre.avatar)"
                  />
                  <li v-if="index != 0" class="li-membre">
                    <span v-if="index != 0" class="nom-membre"
                      >{{ membre.nom }}
                    </span>
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
      v-model="dialogInfosGroupe"
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
            <el-select class="m-2" v-model="this.label" size="large">
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
              <img :src="this.groupe.photo" />
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
              @click="updateGroup()"
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
import { Flag } from "@element-plus/icons-vue";
const dialogInfosGroupe = ref(false);
const dialogInfosContenu = ref(false);
const ruleFormRef = ref<FormInstance>();

export default {
  data() {
    return {
      groupe: [],
      user_admin: [],
      user_connecte: [],
      users_find: [],
      tab_users_list: [],
      tab_members_list: [],
      tab_id_members: [],
      string_entered: "",
      avatar_groupe_src: "",
      label: "",
      request_not_null: false,
      rules: reactive({
        nom: [{ validator: this.checkNom, trigger: "blur", required: true }],
        avatar: [
          { validator: this.checkAvatar, trigger: "blur", required: true },
        ],
      }),
    };
  },
  watch: {
    string_entered: function (value) {
      this.searchUser(value);
    },
  },
  methods: {
    changeImg(e) {
      this.groupe.photo = e;
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

    findLabelOfGroupWithSrc(src) {
      const groupObject = iconForGroup.filter((group) => group.photo === src);
      return groupObject[0].label;
    },

    findSrcOfAvatarWithLabel(label) {
      const avatarObject = avatarForUser.filter(
        (avatar) => avatar.label === label
      );
      return avatarObject[0].photo;
    },
    async findSrcOfGroupWithLabel() {
      const groupeOject = iconForGroup.filter(
        (groupe) => groupe["label"] === this.label
      );
      this.avatar_groupe_src = groupeOject[0].photo;
    },
    updateGroup() {
      this.dialogInfosGroupe = false;
      const token = JSON.parse(localStorage.getItem("user"));
      // ENLEVER LE CHAMP : "membres_groupes" de this.groupe
      delete this.groupe["membres_groupe"];
      // FORME DE L'OBJET this.groupe a changé : JSON.stringify?
      console.log(this.groupe);
      this.groupe.membres = this.tab_id_members;
      GroupsService.updateGroup(token, this.groupe["id"], this.groupe);
      this.groupe["membres_groupe"] = [];
      this.getInfosMembreGroupe();
    },
    async getInfosMembreGroupe() {
      const token = JSON.parse(localStorage.getItem("user"));

      for (let i = 0; i < this.groupe.membres.length; i++) {
        if (this.groupe.membres[i] == this.groupe.admin) {
          this.user_admin = await userService.getSpecificUser(
            token,
            this.groupe.membres[i]
          );
        }
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
    estAdmin(user, groupe) {
      return user.id == groupe.admin;
    },
    async searchUser(string_entered) {
      const token = JSON.parse(localStorage.getItem("user"));

      const users = await userService.getUsersWithStringEntered(
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
      userService.updateUser(JSON.parse(localStorage.getItem("user")), user);
    },
    getMembresToUpdate(groupe) {
      const token = JSON.parse(localStorage.getItem("user"));
      groupe.membres.forEach(async (element, index) => {
        if (index != 0) {
          let user = await userService.getSpecificUser(token, element);
          this.addToMembersList(user);
        }
      });
    },
  },
  async mounted() {
    const token = JSON.parse(localStorage.getItem("user"));
    this.user_connecte = await userService.getUser(token);

    this.tab_members_list.push(this.user_connecte);
    this.tab_id_members.push(this.user_connecte.id);

    this.groupe = await GroupsService.getGroup(token, this.$route.query.ref);
    this.getInfosMembreGroupe();
    this.groupe["membres_groupe"] = [];
    this.getMembresToUpdate(this.groupe);
    this.avatar_groupe_src = this.groupe.photo;
    this.label = this.findLabelOfGroupWithSrc(this.avatar_groupe_src) 
  },
  computed: {
    isComplete() {
      return this.groupe.nom && this.label && this.groupe.membres;
    },
  },
};
</script>


<script lang="ts" setup>
import { Edit } from "@element-plus/icons-vue";
import GroupsService from "../services/GroupsService";
import userService from "../services/userService";

const ruleForm = reactive({
  nom: "",
  photo: "",
  membres: "",
  admin: "",
});
</script>

<style lang="scss" scoped>
@import "../assets/constant.scss";


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

.el-icon {
  color: #faa427;
}
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

.admin-li {
  display: flex;
  border: 1px solid $yellow;
  padding-right: 5px;
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