<template>
  <div>
    <el-button
      class="btn-register-login"
      type="warning"
      size="large"
      @click="dialogVisible = true"
      round
    >
      Inscription
    </el-button>

    <el-dialog custom-class="dialog" v-model="dialogVisible" width="35%">
      <img
        class="imgForm"
        :style="{ maxWidth: '30%' }"
        src="/src/components/icon/utilIcon/logo.svg"
      />

      <span class="title"> Inscription</span>

      <div class="formulaire">
        <el-form
          label-position="top"
          ref="ruleFormRef"
          :model="ruleForm"
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
                name="prenom"
              />
            </el-form-item>

            <el-form-item label="Nom" prop="nom" style="width: 47%">
              <el-input
                input-style="font-family:'Raleway', sans-serif; font-weight: bold;"
                v-model="ruleForm.nom"
                placeholder="Nom"
              />
            </el-form-item>
          </div>

          <el-form-item label="Date de naissance" prop="ddn">
            <el-date-picker
              v-model="ruleForm.ddn"
              type="date"
              placeholder="Date de naissance"
              style="width: 100%"
            />
          </el-form-item>
          <el-form-item prop="email" label="Adresse email">
            <el-input
              input-style="font-family:'Raleway', sans-serif; font-weight: bold;"
              name="email"
              v-model="ruleForm.email"
              placeholder="Adresse email"
            />
          </el-form-item>

          <el-form-item prop="mdp" label="Mot de passe">
            <el-input
              v-model="ruleForm.mdp"
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
              v-model="ruleForm.checkPass"
              name="password"
              type="password"
              placeholder="Mot de passe"
              show-password
              autocomplete="off"
            />
          </el-form-item>
          <el-form-item prop="avatar" label="Avatar">
            <el-select
              v-model="ruleForm.avatar"
              class="m-2"
              :placeholder="this.defaultLabel"
              size="large"
            >
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
              <img :src="this.findSrcOfAvatarWithLabel(defaultLabel)" />
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
              @click="register()"
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
import ProfilManager from "./ProfilManager.vue"
import AuthService  from "../services/authService.js";

export default {
  data() {
    return {
      defaultLabel: "Avatar",
      listImages: [],
    };
  },
  methods: {
    findLabelOfAvatarWithSrc(src) {
      if (src.substring(0, 1) !== ".") {
        src = "." + src;
      }
      const avatarObject = avatarForUser.filter(
        (avatar) => avatar.photo === src
      );
      return avatarObject[0].label;
    },

    findSrcOfAvatarWithLabel(label) {
      const avatarObject = avatarForUser.filter(
        (avatar) => avatar["label"] === label
      );
      return avatarObject[0].photo;
    },
    changeImg(e) {
      this.defaultLabel = this.findLabelOfAvatarWithSrc(e);
    },
    register() {
      delete this.ruleForm["checkPass"];
      AuthService.register(this.ruleForm);
    }
  },
  

  computed: {
    isComplete() {
      return (
        this.ruleForm.prenom &&
        this.ruleForm.email &&
        this.ruleForm.nom &&
        this.ruleForm.ddn &&
        this.ruleForm.mdp &&
        this.ruleForm.checkPass
      );
    },
  },
};
</script>


<script lang="ts" setup>
import { ref, reactive } from "vue";
import { ElMessageBox } from "element-plus";
import { FormInstance } from "element-plus";
import { avatarForUser } from "./data/avatarForUser";

const dialogVisible = ref(false);
const inputMail = ref("");
const inputMdp = ref("");
const ruleFormRef = ref<FormInstance>();

const calculateAgeFromDate = (birthday: any) => {
  // birthday is a date
  var ageDifMs = Date.now() - birthday.getTime();
  var ageDate = new Date(ageDifMs); // miliseconds from epoch
  return Math.abs(ageDate.getUTCFullYear() - 1970);
};

const isDateBeforeToday = (date) => {
  if (date) {
    return new Date(date.toDateString()) < new Date(new Date().toDateString());
  }
};

const checkAge = (rule: any, value: any, callback: any) => {
  setTimeout(() => {
    if (!value) {
      callback(new Error("Veuillez choisir une date."));
    }
    if (!isDateBeforeToday(value)) {
      callback(new Error("Veuillez choisir une date de naissance correcte."));
    } else {
      if (calculateAgeFromDate(value) < 18) {
        callback(new Error("Vous devez avoir plus de 18 ans."));
      } else {
        callback();
      }
    }
  }, 1000);
};

const checkPrenom = (rule: any, value: any, callback: any) => {
  if (!value || value === "") {
    callback(new Error("Veuillez saisir un prénom."));
  }
};

const checkNom = (rule: any, value: any, callback: any) => {
  if (!value || value === "") {
    callback(new Error("Veuillez saisir un nom."));
  }
};

const checkAvatar = (rule: any, value: any, callback: any) => {
  if (!value || value === "") {
    callback(new Error("Veuillez choisir un avatar."));
  }
};

const validatePass = (rule: any, value: any, callback: any) => {
  if (value === "") {
    callback(new Error("Veuillez saisir un mot de passe"));
  } else {
    if (ruleForm.mdp !== "") {
      if (value.length < 6 || !/\d/.test(value)) {
        callback(
          new Error(
            "Votre mot de passe doit être composé d'au moins 6 caractères et d'au moins un chiffre"
          )
        );
      }
      if (!ruleFormRef.value) return;
      ruleFormRef.value.validateField("checkPass", () => null);
    }
    callback();
  }
};
const validatePass2 = (rule: any, value: any, callback: any) => {
  if (value === "") {
    callback(new Error("Réessayez"));
  } else if (value !== ruleForm.mdp) {
    callback(new Error("Les mots de passe sont différents"));
  } else {
    callback();
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
  prenom: [{ validator: checkPrenom, trigger: "blur", required: true }],
  nom: [{ validator: checkNom, trigger: "blur", required: true }],
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
  ddn: [{ validator: checkAge, trigger: "blur", required: true }],
  mdp: [{ validator: validatePass, trigger: "blur", required: true }],
  checkPass: [{ validator: validatePass2, trigger: "blur", required: true }],
  avatar: [{ validator: checkAvatar, trigger: "blur", required: true }],
});
</script>


<style scoped lang="scss">
@import "../assets/constant.scss";

.iconGrid {
  display: grid;
  grid-template-columns: auto auto auto;
}

.el-select-dropdown__item {
  height: 55px !important;
}

.dialog {
  background-color: $gray !important;
  border-radius: 5px;
}

.el-dialog__header {
  display: flex;
  font-weight: bold;
  margin-right: 0px !important;
}

.el-dialog__body {
  display: grid;
  padding-bottom: 0px !important;
  padding-bottom: 200px !important;
}

.el-dialog__title {
  margin-left: auto;
  margin-right: auto;
}

.dialog-footer button:first-child {
  margin-right: 10px;
}

.el-dialog__close {
  color: white !important;
}

.imgForm {
  display: flex;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 25px;
}

.title {
  display: flex;
  margin-left: auto;
  margin-right: auto;
  font-weight: bold;
  margin-bottom: 10px;
  font-size: 24px;
  color: white;
  margin-top: -10px;
}

.formulaire {
  margin-top: 30px;
  width: 80%;
  margin-left: auto;
  margin-right: auto;
}

.el-form-item__label {
  font-weight: 1000;
  font-size: 18px;
}

@media screen and (max-width: 800px) {
  .el-form-item {
    width: 100% !important;
  }
}
.el-form-item {
  margin-bottom: 20px !important;
}

.names {
  display: flex;
}

.el-form-item__error {
  color: red;
}

.el-avatar {
  margin-left: 5%;
}

@media screen and (max-width: 715px) and (min-width: 600px) {
  .el-form-item__label {
    font-size: 14px;
  }
}

@media screen and (max-width: 599px) {
  .el-form-item__label {
    font-size: 14px;
  }
}

@media screen and (max-width: 1200px) and (min-width: 601px) {
  .dialog {
    min-width: 90% !important;
  }
}

@media screen and (max-width: 600px) {
  .dialog {
    min-width: 70% !important;
  }
}

@media screen and (max-width: 800px) {
  .names {
    display: block;
  }
}

@media screen and (max-width: 1313px) {
  .el-avatar {
    margin-left: auto !important;
    margin-right: auto !important;
    margin-top: 10px;
  }

  .el-select {
    width: 100%;
  }
}

.el-input__inner {
  font-family: Raleway, sans-serif !important;
  font-weight: bold !important;
}

input {
  font-family: "Raleway", sans-serif !important;
  font-weight: bold !important;
}
</style>

<style>
.btn-register-login {
  font-size: 20px;
  font-weight: bold;
}

.el-form-item__label {
  margin-bottom: 5px !important;
}

</style>

