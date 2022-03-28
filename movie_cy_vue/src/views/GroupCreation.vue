<script setup>
import SideBar from "../components/SideBar.vue";
import ToolBar from "../components/ToolBar.vue";
import AddGroupMembers from "../components/AddGroupMembers.vue";
import CreationGroupForm from "../components/CreationGroupForm.vue";
</script>

<template>
  <div>
    <SideBar />
    <div class="content-group">
      <div class="toolbar">
        <ToolBar />
      </div>
      <div class="form">
        <CreationGroupForm />
        <AddGroupMembers />
      </div>
    </div>
  </div>
</template>

<style scoped>
.toolbar {
  margin-left: 10%;
  margin-right: 3%;
  height: 50px;
}

.content-group {
  margin-right: 56px;
}
</style>
