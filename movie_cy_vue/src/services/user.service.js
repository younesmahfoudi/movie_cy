import api from "./api";
import VueJwtDecode from "vue-jwt-decode";

class UserService {
  getUser(userToken) {
    return api
      .get(`/users/${VueJwtDecode.decode(userToken)}`)
      .then((res) => console.log(res));
  }
}

export default new UserService();
