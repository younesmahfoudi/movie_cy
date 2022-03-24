<template >
  <button @click="fetchUsers">click me</button>
</template>

<script lang="ts">
import axios from 'axios';
export default {
  name: "app",
  data() {
    return {
      users: [],
    };
  },
  methods: {
    fetchUsers: function () {
      const baseURI = "http://localhost:8000/users/";
      axios.get(baseURI).then((result) => {
        console.log(result)
      });
    },
  },
};
</script>

<style lang="scss">
@import "../assets/constant.scss";

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
