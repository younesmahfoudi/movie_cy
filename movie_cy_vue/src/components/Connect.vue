<template>
  <div>
    <el-button class='btn-register-login' type="warning" size="large" @click="dialogVisible = true" round>
      Connexion
    </el-button>

    <el-dialog custom-class="dialog" v-model="dialogVisible" width="30%">
      <img
        class="imgForm"
        :style="{ maxWidth: '30%' }"
        src="/src/components/icon/utilIcon/logo.svg"
      />

      <span class="title"> Connexion</span>

      <div class="formulaire">
        <el-form model="formLogin" label-position="top">
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
              input-style="border-radius:20px; font-family:'Raleway', sans-serif; font-weight: bold;"
              name="email"
              v-model="inputMail"
              placeholder="Adresse email"
            />
          </el-form-item>

          <el-form-item
            prop="password"
            label="Mot de passe"
            :rules="[
              {
                required: true,
                message: 'Entrer un mot de passe.',
                trigger: 'blur',
              },
            ]"
          >
            <el-input
              input-style="border-radius:20px ; font-family:'Raleway', sans-serif; font-weight: bold;"
              name="password"
              v-model="inputMdp"
              type="password"
              placeholder="Mot de passe"
              show-password
            />
          </el-form-item>
        </el-form>
      </div>

      <template #footer>
        <div style="display: flex">
          <span class="dialog-footer">
            <el-button
              type="warning"
              class="btnValider validate"
              @click="dialogVisible = false"
              round
              >Valider</el-button
            >
          </span>
        </div>
      </template>
    </el-dialog>
  </div>
</template>

<script lang="ts" setup>
import { ref } from "vue";
const dialogVisible = ref(false);
const inputMail = ref("");
const inputMdp = ref("");
</script>

<style lang="scss">
@import "../assets/constant.scss";

.validate{
  font-size : 20px!important;
  font-weight: bold;
}

.dialog {
  background-color: $gray !important;
  border-radius: 10px;
}

.el-dialog__header {
  display: flex;
  font-weight: bold;
  margin-right: 0px !important;
}

.el-dialog__body {
  display: grid;
  padding-bottom: 0px!important;
  padding-top: 0px!important;
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

.el-form-item {
  margin-bottom: 40px !important;
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

@media screen and (max-width: 1400px) and (min-width: 601px) {
  .dialog {
    min-width: 50% !important;
  }
}

@media screen and (max-width: 600px) {
  .dialog {
    min-width: 70% !important;
  }
}

.dialog-footer {
  margin-left: auto !important;
  margin-right: auto !important;
}
</style>

<style scoped>
@media screen and (max-width: 1000px) and (min-width: 601px) {
  .dialog {
    min-width: 50% !important;
  }
}
</style>