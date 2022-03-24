import { createApp } from "vue";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import fr from 'element-plus/es/locale/lang/fr'
import App from "./App.vue";
import router from "./router";

const app = createApp(App);

app.use(router);

app.use(ElementPlus, {
    locale : fr
});
app.mount("#app");
