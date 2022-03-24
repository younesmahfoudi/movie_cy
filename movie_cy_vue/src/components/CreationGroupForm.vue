<template>
  <div class="formulaire">
    <el-form :model="form" label-position="top" label-width="120px">
      <el-form-item label="Nom du groupe">
        <el-input v-model="form.name" />
      </el-form-item>

      <el-form-item label="Image du groupe">
        <el-select
          @change="(e) => changeImg(e)"
          v-model="value"
          class="m-2"
          placeholder="Choisir une image de groupe"
          size="large"
        >
          <div class="iconGrid">
            <el-option
              v-for="item in options"
              :key="item.value"
              :value="item.photo"
              :label="item.label"
            >
              <div class="oneGroup">
                <el-avatar
                  class="iconGroup"
                  :style="{ backgroundColor: '#faa427' }"
                  :size="48"
                  :src="item.photo"
                />
              </div>
            </el-option>
          </div>
        </el-select>
        <el-avatar
          class="iconGroup avatarHidden"
          id="iconChoosenForChange"
          :style="{ backgroundColor: '#faa427' }"
          :size="48"
        >
          <img id="img" />
        </el-avatar>
      </el-form-item>
    </el-form>
  </div>
</template>


<script>
export default {
  methods: {
    changeImg(e) {
      document.getElementById("img").src = e;
      document.getElementById("iconChoosenForChange").className +=
        " avatarVisible";
    },
  },
};
</script>

<script setup>
import { reactive } from "vue";
import { ref } from "vue";

const form = reactive({
  name: "",
  region: "",
  date1: "",
  date2: "",
  delivery: false,
  type: [],
  resource: "",
  desc: "",
});

const value = ref("");

const options = [
  {
    value: "Option1",
    label: "Pistolet",
    photo: "./src/components/icon/ThemeIcon/action.png",
  },
  {
    value: "Option2",
    label: "Mickey",
    photo: "./src/components/icon/ThemeIcon/animation.png",
  },
  {
    value: "Option3",
    label: "Boussole",
    photo: "./src/components/icon/ThemeIcon/aventures.png",
  },
  {
    value: "Option4",
    label: "Comédie",
    photo: "./src/components/icon/ThemeIcon/comedie.png",
  },
  {
    value: "Option5",
    label: "Loupe",
    photo: "./src/components/icon/ThemeIcon/detective.png",
  },
  {
    value: "Option6",
    label: "Caméra",
    photo: "./src/components/icon/ThemeIcon/docu.png",
  },
  {
    value: "Option7",
    label: "Drame",
    photo: "./src/components/icon/ThemeIcon/drame.png",
  },
  {
    value: "Option8",
    label: "Espion",
    photo: "./src/components/icon/ThemeIcon/espion.png",
  },
  {
    value: "Option9",
    label: "Baguette magique",
    photo: "./src/components/icon/ThemeIcon/fantaisie.png",
  },
  {
    value: "Option10",
    label: "Chapeau",
    photo: "./src/components/icon/ThemeIcon/filmNoir.png",
  },
  {
    value: "Option11",
    label: "Sablier",
    photo: "./src/components/icon/ThemeIcon/histoire.png",
  },
  {
    value: "Option12",
    label: "Couteau",
    photo: "./src/components/icon/ThemeIcon/horreur.png",
  },
  {
    value: "Option13",
    label: "Musique",
    photo: "./src/components/icon/ThemeIcon/musical.png",
  },
  {
    value: "Option14",
    label: "Cactus",
    photo: "./src/components/icon/ThemeIcon/occidental.png",
  },
  {
    value: "Option15",
    label: "Coeur",
    photo: "./src/components/icon/ThemeIcon/romance.png",
  },
  {
    value: "Option16",
    label: "Socoupe",
    photo: "./src/components/icon/ThemeIcon/scifi.png",
  },
  {
    value: "Option17",
    label: "Rugby",
    photo: "./src/components/icon/ThemeIcon/sport.png",
  },
  {
    value: "Option18",
    label: "Crâne",
    photo: "./src/components/icon/ThemeIcon/thriller.png",
  },
];

const onSubmit = () => {
};
</script>

<style lang="css" scoped>
.iconGroup {
  margin-left: auto;
  margin-right: auto;
  display: block;
}

.el-select-dropdown__item {
  height: 55px !important;
}

.iconGrid {
  display: grid;
  grid-template-columns: auto auto auto;
}

.oneGroup {
  padding-top: 5px;
}

.avatarHidden {
  visibility: hidden;
}

.avatarVisible {
  visibility: visible;
}
.formulaire{
  max-width: 50%;
  margin-left: 10% !important;
}
#iconChoosenForChange{
  margin: 0 !important;
}
</style>