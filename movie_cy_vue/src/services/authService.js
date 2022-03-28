import axios from "axios";
const API_URL = "http://localhost:8000/";
class AuthService {
  login(user) {
    return axios
      .post(API_URL + "login", {
        email: user.email,
        mdp: user.mdp,
      })
      .then((response) => {
        console.log(response);
        if (response.data[0].access_token) {
          localStorage.setItem("user", JSON.stringify(response.data[1]));
        }
        return response.data;
      });
  }
  logout() {
    localStorage.removeItem("user");
  }
  register(user) {
    return axios.post(API_URL + "users/signup", user).then((response) => {
      console.log(response);

      if (response.data[0].access_token) {
        localStorage.setItem("user", JSON.stringify(response.data[1]));
      }
      return response.data;
    });
  }
}
export default new AuthService();
