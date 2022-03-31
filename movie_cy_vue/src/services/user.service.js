import api from "./api";
import VueJwtDecode from "vue-jwt-decode";

class UserService {
  getUser(userToken) {
    return api
      .get(`/users/${VueJwtDecode.decode(userToken.access_token).user_id}`)
      .then((response) => response.data.data[0]);
  }
}

export default new UserService();
