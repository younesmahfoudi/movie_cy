<script setup>
import CreationGroupForm from "./components/CreationGroupForm.vue";
import Connect from "./components/Connect.vue";
import RegisterForm from "./components/RegisterForm.vue";




</script>

<template>
<div>
  <CreationGroupForm />
  <Connect/>
  <RegisterForm/>
</div>
</template>


<style lang="scss">
@import "src/assets/constant.scss";
body{
  font-family: $font;
}
</style>
