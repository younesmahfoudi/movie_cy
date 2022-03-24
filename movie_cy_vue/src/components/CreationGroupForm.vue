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

      <el-form-item prop="avatar" label="Image du groupe">
        <el-select
          @change="(e) => changeImg(e)"
          v-model="ruleForm.avatar"
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
          :size="60"
        >
          <img :src="imageSrc" />
        </el-avatar>
      </el-form-item>
    </el-form>
    <el-button
      class="validate"
      type="warning"
      @click="createUser()"
      round
      :disabled="!isComplete"
    >
      Valider
    </el-button>
  </div>
</template>


<script lang="ts">
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
      //UsersService.createUser(this.ruleForm);
    },
  },
  computed: {
    isComplete() {
      return (
        this.ruleForm.nom &&
        this.ruleForm.avatar
      );
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
  avatar: "",
});

const checkNom = (rule: any, value: any, callback: any) => {
  if (!value || value === "") {
    callback(new Error("Veuillez saisir un nom de groupe"));
  }
};

const checkAvatar = (rule: any, value: any, callback: any) => {
  debugger;
  if (!value || value === "") {
    callback(new Error("Veuillez choisir un avatar."));
  }
};

const rules = reactive({
  nom: [{ validator: checkNom, trigger: "blur", required: true }],
  avatar: [{ validator: checkAvatar, trigger: "blur", required: true }],
});

const value = ref("");
</script>

<style lang="css" scoped>
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
  grid-template-columns: auto auto auto;
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
}
</style>