<script setup>
import ToolBar from "../components/ToolBar.vue";
import AddGroupMembers from "../components/AddGroupMembers.vue";
import CreationGroupForm from "../components/CreationGroupForm.vue";
</script>

<template>
  <div class="content">
    <div class="toolbar">
      <ToolBar />
    </div>
    <div class="form">
      <CreationGroupForm />
      <AddGroupMembers />
    </div>
  </div>
</template>

<style>
.toolbar {
  margin-left: 10%;
  margin-right: 3%;
  height: 50px;
}

.content {
  margin-left: 10%;
  margin-top: 3%;
  margin-bottom: 3%;
  margin-right: 3%;
}
</style>
