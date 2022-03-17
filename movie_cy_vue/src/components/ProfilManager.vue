<template>
  <div id="profil">   
    <div class="common-layout">
        <el-container>
        <el-container>
            <el-header>  
            <div id="header-monprofil">
                <div> USERNAME  </div>  
                <div> <el-avatar :size="50" :src="circleUrl" />
                </div>
            </div>
            </el-header>
            <el-main>
                <div>
                    <ul>
                        <li> Mon type préféré: </li>
                        <li> Mon second type préféré: </li>
                        <li> Mon acteur preferé: </li>
                        <li> Mon réalisateur preferé: </li>
                    </ul>       
                </div>
                <el-button type="warning">Modifier</el-button>
            </el-main>
        </el-container>
        </el-container>
    </div>
  </div> 
</template>

<style>
#header-monprofil{
    display: flex;
    justify-content: space-between;
    width: 100%;
}
#profil{
    display: block;
    width: 400px;
}

#profil ul {
        list-style: none;
}

</style>