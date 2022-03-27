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
        <el-select
          v-model="value"
          multiple
          filterable
          remote
          reserve-keyword
          placeholder="Choisir des utilisateurs"
          :remote-method="remoteMethod"
          :loading="loading"
        >
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          />
        </el-select>
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

export default {
  data() {
    return {
      imageSrc: "./src/components/icon/ThemeIcon/action.png",
      defaultLabel: "Pistolet",
      listImages: [],
    };
  },
  methods: {
    changeImg(e) {
      this.imageSrc = e;
    },
    createGroup() {
      GroupsService.createGroup(this.ruleForm);
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
import { reactive } from "vue";
import { ref } from "vue";
import { iconForGroup } from "./data/iconForGroup";

const ruleForm = reactive({
  nom: "",
  photo: "",
  membres: ["623db4a15a5a69cbe3666ea1"], // A CHANGER AVEC ID DU MEC CONNECTE + LES AUTRES USERS
  admin: "623db4a15a5a69cbe3666ea1", // A CHANGER AVEC ID DU MEC CONNECTE
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
</style>