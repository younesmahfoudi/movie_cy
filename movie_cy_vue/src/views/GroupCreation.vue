<script setup>
import SideBar from "../components/SideBar.vue";
import ToolBar from "../components/ToolBar.vue";
import AddGroupMembers from "../components/AddGroupMembers.vue";
import CreationGroupForm from "../components/CreationGroupForm.vue";
</script>

<template>
  <SideBar />
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

<style scoped>
.toolbar {
  margin-left: 10%;
  margin-right: 3%;
  height: 50px;
}

.content {
  margin-right: 3%;
}
</style>
