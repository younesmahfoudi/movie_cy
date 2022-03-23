<template>
  <div>
    <el-button class='btn-register-login' type="warning" size="large" @click="dialogVisible = true" round>
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
                v-model.number="ruleForm.prenom"
                placeholder="Prénom"
              />
            </el-form-item>

            <el-form-item label="Nom" prop="nom" style="width: 47%">
              <el-input
                input-style="font-family:'Raleway', sans-serif; font-weight: bold;"
                v-model.number="ruleForm.nom"
                placeholder="Nom"
              />
            </el-form-item>
          </div>

          <el-form-item label="Age" prop="age">
            <el-input
              type="number"
              input-style="font-family:'Raleway', sans-serif; font-weight: bold;"
              v-model.number="ruleForm.age"
              placeholder="Age"
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

          <el-form-item prop="pass" label="Mot de passe">
            <el-input
              v-model="ruleForm.pass"
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
              v-model="photo"
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
              :size="60"
            >
              <img :src="imageSrc" />
            </el-avatar>
          </el-form-item>
        </el-form>
      </div>

      <template #footer>
        <div style="display: flex">
          <span class="dialog-footer">
            <el-button class="validate" type="warning" @click="submitForm(ruleFormRef)" round>
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
      imageSrc: "./src/components/icon/CharacterIcon/alien.png",
      defaultLabel: "Alien",
      listImages: [],
    };
  },
  methods: {
    changeImg(e) {
      this.imageSrc = e;
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

const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return;
  formEl.validate((valid) => {
    if (valid) {
      console.log("submit!");
    } else {
      console.log("error submit!");
      return false;
    }
  });
};

const checkAge = (rule: any, value: any, callback: any) => {
  setTimeout(() => {
    if (!value) {
      callback(new Error("Veuillez saisir un âge."));
    }
    if (!Number.isInteger(value)) {
      callback(new Error("Veuillez saisir un nombre correct."));
    } else {
      if (value < 18) {
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
  debugger;
  if (!value || value === "") {
    callback(new Error("Veuillez choisir un avatar."));
  }
};

const validatePass = (rule: any, value: any, callback: any) => {
  if (value === "") {
    callback(new Error("Saisissez votre mot de passe"));
  } else {
    if (ruleForm.checkPass !== "") {
      if (!ruleFormRef.value) return;
      ruleFormRef.value.validateField("checkPass", () => null);
    }
    callback();
  }
};
const validatePass2 = (rule: any, value: any, callback: any) => {
  if (value === "") {
    callback(new Error("Réessayez"));
  } else if (value !== ruleForm.pass) {
    callback(new Error("Les mots de passe sont différents"));
  } else {
    callback();
  }
};

const ruleForm = reactive({
  prenom: "",
  nom: "",
  email: "",
  age: "",
  pass: "",
  checkPass: "",
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
  age: [{ validator: checkAge, trigger: "blur", required: true }],
  pass: [{ validator: validatePass, trigger: "blur", required: true }],
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
  margin-top: -60px;
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
.btn-register-login{
  font-size: 20px;
  font-weight: bold;
}
</style>

