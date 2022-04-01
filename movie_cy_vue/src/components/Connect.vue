<template>
  <div>
    <el-button
      class="btn-register-login"
      type="warning"
      size="large"
      @click="dialogVisible = true"
      round
    >
      Connexion
    </el-button>

    <el-dialog custom-class="dialog dialog-connect" v-model="dialogVisible" width="30%">
      <img
        class="imgForm"
        :style="{ maxWidth: '30%' }"
        src="/src/components/icon/utilIcon/logo.svg"
      />

      <span class="title"> Connexion</span>

      <div class="formulaire">
        <el-form
          ref="ruleFormRef"
          :model="ruleForm"
          :rules="rules"
          label-position="top"
        >
          <el-form-item prop="email" label="Adresse email">
            <el-input
              input-style="border-radius:20px; font-family:'Raleway', sans-serif; font-weight: bold;"
              name="email"
              v-model="ruleForm.email"
              placeholder="Adresse email"
            />
          </el-form-item>

          <el-form-item prop="password" label="Mot de passe">
            <el-input
              input-style="border-radius:20px ; font-family:'Raleway', sans-serif; font-weight: bold;"
              name="password"
              v-model="ruleForm.mdp"
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
              @click="login()"
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
import { ref, reactive } from "vue";
import { FormInstance } from "element-plus";

const dialogVisible = ref(false);
const ruleFormRef = ref<FormInstance>();
</script>

<script lang="ts">
import AuthService  from "../services/auth.service";

export default {
  data: function () {
    return {
      ruleForm : reactive({
        email: "",
        mdp: "",
      })
    }
  },
  methods: {
    login() {
      //AuthService.login(this.ruleForm);
      this.$store.dispatch("auth/login", this.ruleForm).then(
        () => {
          this.$router.push("/profil");
        },
        (error) => {
          console.log(error);
        }
      );
    }
  },
  computed: {
    isComplete() {
      return this.ruleForm.email && this.ruleForm.mdp;
    },
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    },
  },
  created() {
    if (this.loggedIn) {
      this.$router.push("/profil");
    }
  },
};

const rules = reactive({
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
  mdp: [{ trigger: "blur", required: true }],
});
</script>

<style lang="scss">

@import "../assets/constant.scss";

.dialog-connect{
  margin-top: 10%;
}

.validate {
  font-size: 20px !important;
  font-weight: bold;
  margin-bottom: 10px;
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
  padding-bottom: 0px !important;
  padding-top: 0px !important;
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
  margin-bottom: 50px;
}

.title {
  display: flex;
  justify-content: center;
  margin-left: auto;
  margin-right: auto;
  font-weight: bold;
  margin-bottom: 10px;
  font-size: 24px;
  color: white;
  margin-top: -10px;
  word-break: keep-all;
  text-align: center;
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
.el-popper.is-light{
  word-break: keep-all;
}
</style>

<style scoped>
@media screen and (max-width: 1000px) and (min-width: 601px) {
  .dialog {
    min-width: 50% !important;
  }
}
</style>
