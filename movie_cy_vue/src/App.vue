<script setup>
import CreationGroupForm from "./components/CreationGroupForm.vue";
import Connect from "./components/Connect.vue";



</script>

<template>
<div>
  <CreationGroupForm />
  <Connect/>
</div>
</template>


<style lang="scss">
@import "src/assets/constant.scss";
body{
  font-family: $font;
}
</style>
