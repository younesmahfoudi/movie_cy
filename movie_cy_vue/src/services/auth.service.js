import CryptoJS from "crypto-js";
import api from "./api";
import TokenService from "./token.service";

class AuthService {
  login({ email, mdp }) {
    mdp = this.encrypt(mdp);
    return api
      .post("/users/login", {
        email,
        mdp,
      })
      .then((response) => {
        if (response.data.access_token) {
          TokenService.setUser(response.data);
        }
        return response.data;
      });
  }
  logout() {
    TokenService.removeUser();
  }

  register(user) {
    return api
      .post("/users/register", {
        user,
      })
      .then((response) => {
        if (response.data.access_token) {
          TokenService.setUser(response.data);
        }
        return response.data;
      });
  }

  // register(user) {
  //   user.mdp = this.encrypt(user.mdp);
  //   return axios.post(API_URL + "users/signup", user).then((response) => {
  //     if (response.data.access_token) {
  //       localStorage.setItem("user", JSON.stringify(response.data));
  //       router.push("/profil");
  //     }
  //     return response.data;
  //   });
  // }

  encrypt(user) {
    const passphrase = "deff1952d59f883ece260e8683fed21ab0ad9a53323eca4f";
    return CryptoJS.SHA256(user.mdp, passphrase).toString();
  }

  decrypt(user) {
    const passphrase = "deff1952d59f883ece260e8683fed21ab0ad9a53323eca4f";
    const bytes = CryptoJS.SHA256(user.mdp, passphrase);
    const originalText = bytes.toString(CryptoJS.enc.Utf8);
    return originalText;
  }
}
export default new AuthService();
