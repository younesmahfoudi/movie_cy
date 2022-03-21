<template>
  <div>
    <el-button type="text" @click="dialogVisible = true">Inscription</el-button>

    <el-dialog custom-class="dialog" v-model="dialogVisible" width="30%">
      <img class="imgForm" src="./icon/utilIcon/logo.png" />

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
              :rules="[
                {
                  required: true,
                  message: 'Entrer un prénom',
                },
              ]"
            >
              <el-input
                input-style="font-family:'Raleway', sans-serif; font-weight: bold;"
                v-model.number="ruleForm.age"
                placeholder="Prénom"
              />
            </el-form-item>

            <el-form-item
              label="Nom"
              prop="nom"
              style="width: 47%"
              :rules="[
                {
                  required: true,
                  message: 'Entrer un nom',
                },
              ]"
            >
              <el-input
                input-style="font-family:'Raleway', sans-serif; font-weight: bold;"
                v-model.number="ruleForm.age"
                placeholder="Nom"
              />
            </el-form-item>
          </div>

          <el-form-item
            label="Age"
            prop="age"
            :rules="[
              {
                required: true,
              },
            ]"
          >
            <el-input
              type="number"
              input-style="font-family:'Raleway', sans-serif; font-weight: bold;"
              v-model.number="ruleForm.age"
              placeholder="Age"
            />
          </el-form-item>
          <el-form-item
            prop="email"
            label="Adresse email"
            :rules="[
              {
                required: true,
                message: 'Entrer une adresse email.',
                trigger: 'blur',
              },
              {
                type: 'email',
                message: 'Entrer une adresse email correcte.',
                trigger: ['blur', 'change'],
              },
            ]"
          >
            <el-input
              input-style="font-family:'Raleway', sans-serif; font-weight: bold;"
              name="email"
              v-model="inputMail"
              placeholder="Adresse email"
            />
          </el-form-item>

          <el-form-item
            prop="pass"
            label="Mot de passe"
            :rules="[
              {
                required: true,
              },
            ]"
          >
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

          <el-form-item
            prop="checkPass"
            label="Confirmation mot de passe"
            :rules="[
              {
                required: true,
              },
            ]"
          >
            <el-input
              v-model="ruleForm.checkPass"
              input-style="font-family:'Raleway', sans-serif; font-weight: bold;"
              name="password"
              type="password"
              placeholder="Mot de passe"
              show-password
              autocomplete="off"
            />
          </el-form-item>
        </el-form>
      </div>

      <template #footer>
        <div style="display: flex">
          <span class="dialog-footer">
            <el-button class="btnValidate" @click="dialogVisible = false"
              >Valider</el-button
            >
          </span>
        </div>
      </template>
    </el-dialog>
  </div>
</template>


<script lang="ts" setup>
import { ref, reactive } from "vue";
import { ElMessageBox } from "element-plus";
import type { FormInstance } from "element-plus";

const dialogVisible = ref(false);
const inputMail = ref("");
const inputMdp = ref("");
const ruleFormRef = ref<FormInstance>();

const checkAge = (rule: any, value: any, callback: any) => {
  if (!value) {
    return callback(new Error("Please input the age"));
  }
  setTimeout(() => {
    if (!Number.isInteger(value)) {
      callback(new Error("Please input digits"));
    } else {
      if (value < 18) {
        callback(new Error("Age must be greater than 18"));
      } else {
        callback();
      }
    }
  }, 1000);
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
  pass: "",
  checkPass: "",
  age: "",
});

const rules = reactive({
  pass: [{ validator: validatePass, trigger: "blur" }],
  checkPass: [{ validator: validatePass2, trigger: "blur" }],
  age: [{ validator: checkAge, trigger: "blur" }],
});
</script>


<style lang="scss">
@import "../assets/constant.scss";

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
    width: 100%!important;
  }
}
.el-form-item {
  margin-bottom: 20px !important;
}

.names {
  display: flex;
}

.btnValidate {
  background-color: $yellow;
  margin-right: 0px !important;
  font-family: "Raleway", sans-serif;
  font-size: 20px;
  border: none;
}

.el-form-item__error {
  color: red;
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

@media screen and (max-width: 1000px) and (min-width: 601px) {
  .dialog {
    min-width: 50% !important;
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

.el-button--default {
  --el-button-hover-text-color: $grey !important;
}
</style>

<style scoped lang="scss">
.el-dialog__footer {
  display: flex !important;
}

.dialog-footer {
  margin-left: auto !important;
  margin-right: auto !important;
}
</style>

