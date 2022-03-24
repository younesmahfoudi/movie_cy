<template>
  <div class="donnees">
    <el-row :gutter="10">
      <el-col :xs="24" :sm="24" :md="24" :lg="12" :xl="24">
        <div class="username">
          MAXIME

          <el-avatar
            class="iconGroup"
            :style="{ backgroundColor: '#faa427' }"
            :size="90"
          />
        </div>
      </el-col>
    </el-row>

    <el-row :gutter="10">
      <el-col :xs="24" :sm="24" :md="24" :lg="12" :xl="12">
        <div class="username">
          <el-descriptions title="Vos informations">
            <el-descriptions-item label="Prénom :"
              >Maxime</el-descriptions-item
            >
            <el-descriptions-item label="Nom :"
              >Adda</el-descriptions-item
            >
            <el-descriptions-item label="Âge"
              >23</el-descriptions-item
            >
            <el-descriptions-item label="Adresse email">
              maxime.adda@hotmail.fr
            </el-descriptions-item>
          </el-descriptions>
        </div>
      </el-col>
    </el-row>
    <div style="display: flex">
      <el-button type="primary" class="btnValider"
        >Modifier ces informations</el-button
      >
    </div>
  </div>
</template>

<style lang="scss">
@import "../assets/constant.scss";

.el-descriptions__cell {
  width: 100%;
}
tr {
  display: flex;
  flex-wrap: wrap;
}

.username {
  font-size: 60px;
  display : flex
}

.btnValider {
  background-color: $yellow;
  margin-right: 0px !important;
  border: none;
  border-radius: 20px;
  font-family: "Raleway", sans-serif;
  font-weight: bold;
  font-size: 20px;
}



.donnees {
  margin: 5%;
}

.el-avatar{
    margin-left: 10%;
}
.el-descriptions__cell {
    font-size: 20px!important;
}
</style>

<style scoped lang="scss">
.el-descriptions__cell {
  width: 100%;
}

td {
  width: 100%;
}


</style>