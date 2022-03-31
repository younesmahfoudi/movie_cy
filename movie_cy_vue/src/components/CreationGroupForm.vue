<template>
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

      <el-form-item prop="photo" label="Image du groupe">
        <el-col :span="22">
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
        </el-col>
        <el-col :span="2">
          <el-avatar
            v-if="imageSrc !== ''"
            class="iconGroup"
            id="iconChoosenForChange"
            :style="{ backgroundColor: '#faa427' }"
            :size="70"
          >
            <img :src="imageSrc" />
          </el-avatar>
        </el-col>
      </el-form-item>
 
      <el-form-item prop="membres" label="Membres du groupe">
     
     
      <el-input v-model="string_entered" placeholder="Chercher des utilisateurs" />

      <div class="div-add-and-research-user">

        <el-card class="box-card">
          <template #header>
              <div class="card-header">
                <span>Utilisateurs</span>
              </div>
          </template>
          <div v-if="this.request_not_null">
            <div v-for="user in this.tab_members_left" :key="user" class="text item">
             <div> <el-button type="primary" @click="addToMembersList(user)" round>+</el-button>  {{ user.prenom + " " + user.nom + " ( " + user.email + " )" }} </div> 
            </div>
          </div>
          <div v-if="!this.request_not_null">
            <span> Aucun utilisateur trouvé</span>
          </div>
        </el-card>

        <el-card class="box-card">
          <template #header>
              <div class="card-header">
                <span>Membres</span>
              </div>
          </template>
          <div v-for="(user,index) in this.tab_members_right" :key="user" class="text item">
             <div v-if="(index==0)"> Admin : {{ user.prenom + " " + user.nom + " ( " + user.email + " )" }} </div>
             <div v-if="(index!=0)">  <el-button type="danger"  @click="removeToMembersList(user)" round>-</el-button> {{ user.prenom + " " + user.nom + " ( " + user.email + " )" }}</div>
          </div>
        
        </el-card>

      </div>
  
      </el-form-item>
    </el-form>


    <el-button
      class="validate"
      type="warning"
      @click="createGroup()"
      round
      :disabled="!isComplete"
    >
      Valider
    </el-button>




  
  </div>

  

</template>


<script lang="ts">
import GroupsService from "../services/GroupsService.js";
import  axios  from "axios";
import UserService from "../services/userService.js";

export default {
  data() {
    return {
      imageSrc: "./src/components/icon/ThemeIcon/action.png",
      defaultLabel: "Pistolet",
      listImages: [],
      users_result: [],
      tab_members_left: [],
      tab_members_right : [],
      tab_id_members: [],
      string_entered : "",
      request_not_null : false,
    };
  },
  async mounted() {
      const token = JSON.parse(localStorage.getItem("user"));
      let user = await userService.getUser(token);
      this.tab_members_right.push(user);
      this.tab_id_members.push(user["id"]);
    
  },
  watch: {
    string_entered: function (value) {
      this.searchUser(value);
    }
  },
  methods: {
    changeImg(e) {
      this.imageSrc = e;
    },
    async createGroup() {
  

      this.ruleForm.membres = this.tab_id_members;
      this.ruleForm.admin = this.tab_id_members[0];
      
      const new_groupe = await GroupsService.createGroup(JSON.parse(localStorage.getItem("user")),this.ruleForm);

      for(var i = 0; i < this.tab_members_right.length; i++){
          this.tab_members_right[i]["groupes"].push(new_groupe.data.data[0]["id"]);
          // console.log(JSON.stringify(this.tab_members_right[i]));
          // console.log(JSON.parse(localStorage.getItem("user")));
          UserService.updateUser(JSON.parse(localStorage.getItem("user")),JSON.parse(JSON.stringify(this.tab_members_right[i])));
      }
    },
    searchUser(string_entered){

      this.request = "http://localhost:8000/users/?string_entered=" + string_entered;
      axios
        .get(this.request)
        .then((response) => {
          if((response.data[0]!=undefined)&&(string_entered!='')&&(string_entered[0]!=' ')){
            this.request_not_null = true; 
            this.users_result = response.data;
            //Vérifie qu'on ait pas deux fois les mêmes utilisateurs dans les deux tableaux
            for(var i =0;i<this.users_result.length;i++){
                for(var j =0;j<this.tab_members_right.length;j++){
                  if(this.users_result[i]["id"] == this.tab_members_right[j]["id"]) {
                    this.users_result.splice(i,1);
                  }
                }
            }
            this.tab_members_left = this.users_result;
          }else{
            this.request_not_null = false; 
          }
          
        });
      
    },
    arrayRemove(arr, value) { 
        return arr.filter(function(ele){ 
            return ele != value; 
        });
    },
    addToMembersList(user) {
      this.tab_members_right.push(user);
      this.tab_id_members.push(user["id"]);
      this.tab_members_left = this.arrayRemove(this.tab_members_left, user);
    },
    removeToMembersList(user) {
      this.tab_members_left.push(user);
      this.tab_id_members = this.arrayRemove(this.tab_id_members, user["id"]);
      this.tab_members_right = this.arrayRemove(this.tab_members_right, user);
    },
    updateGroupsUser(user) {
      UserService.updateUser(JSON.parse(localStorage.getItem("user")),user)
    }
  },
  computed: {
    isComplete() {
      return this.ruleForm.nom;
    },
  },
};
</script>

<script lang="ts" setup>
import { reactive } from "vue";
import { ref } from "vue";
import { iconForGroup } from "./data/iconForGroup";
import userService from '../services/userService.js';


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
  debugger;
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
.formulaire {
  max-width: 50%;
  margin-left: 10% !important;
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

.div-add-and-research-user{
  display: flex;

}

</style>