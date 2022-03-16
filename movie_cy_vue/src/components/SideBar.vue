<template>
  <el-col :span="3">
    <el-menu
      active-text-color="#faa427"
      background-color="#5a6075"
      class="el-menu-vertical-demo"
      default-active="2"
      text-color="#ffffff"
      :style="{ height: '100%' }"
    >
      <el-menu-item index="1">
        <el-avatar
          :style="{ backgroundColor: '#faa427' }"
          :size="50"
          src="./src/components/icon/utilIcon/logo.png"
        />
      </el-menu-item>
      <el-menu-item index="1">
        <el-avatar
          :style="{ backgroundColor: '#faa427' }"
          :size="50"
          src="./src/components/icon/ThemeIcon/animation.png"
        />
      </el-menu-item>
      <el-menu-item index="2">
        <el-avatar
          :style="{ backgroundColor: '#faa427' }"
          :size="50"
          src="./src/components/icon/ThemeIcon/action.png"
        />
      </el-menu-item>
      <el-menu-item index="3">
        <el-avatar
          :style="{ backgroundColor: '#faa427' }"
          :size="50"
          src="./src/components/icon/ThemeIcon/thriller.png"
        />
      </el-menu-item>
      <el-menu-item index="3">
        <el-avatar
          :style="{ backgroundColor: '#faa427' }"
          :size="50"
          src="./src/components/icon/utilIcon/plus.png"
        />
      </el-menu-item>
    </el-menu>
  </el-col>
</template>

<style lang="css" scoped></style>
