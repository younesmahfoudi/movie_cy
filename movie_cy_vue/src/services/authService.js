import axios from "axios";
import CryptoJS from "crypto-js";

const API_URL = "http://localhost:8000/";
class AuthService {
  login(user) {
    return axios
      .post(API_URL + "users/login", {
        email: user.email,
        mdp: this.encrypt(user.mdp),
      })
      .then((response) => {
        console.log(response);
        if (response.data.access_token) {
          localStorage.setItem("user", JSON.stringify(response.data));
        }
        return response.data;
      });
  }

  logout() {
    localStorage.removeItem("user");
  }

  register(user) {
    user.mdp = this.encrypt(user.mdp);
    return axios.post(API_URL + "users/signup", user).then((response) => {
      console.log(response);
      if (response.data.access_token) {
        localStorage.setItem("user", JSON.stringify(response.data));
      }
      return response.data;
    });
  }

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
