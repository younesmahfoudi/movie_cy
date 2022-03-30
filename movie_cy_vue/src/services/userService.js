import axios from "axios";
import VueJwtDecode from "vue-jwt-decode";

class UserService {
  getUser(token) {
    return axios
      .get(
        `http://localhost:8000/users/${
          VueJwtDecode.decode(token.access_token).user_id
        }`,
        {
          headers: {
            Authorization: `Bearer ${token.access_token}`,
          },
        }
      )
      .then((response) => response.data.data[0]);
  }

  getSpecificUser(token, user_id) {
    return axios
      .get(`http://localhost:8000/users/` + user_id, {
        headers: {
          Authorization: `Bearer ${token.access_token}`,
        },
      })
      .then((response) => response.data.data[0]);
  }

  updateUser(token, user) {
    return axios
      .put(
        `http://localhost:8000/users/${
          VueJwtDecode.decode(token.access_token).user_id
        }`,
        user,
        {
          headers: {
            Authorization: `Bearer ${token.access_token}`,
          },
        }
      )
      .then((response) => {
        console.log(response);
        return response;
      });
  }

  deleteUser(token) {
    return axios
      .delete(
        `http://localhost:8000/users/${
          VueJwtDecode.decode(token.access_token).user_id
        }`,
        {
          headers: {
            Authorization: `Bearer ${token.access_token}`,
          },
        }
      )
      .then((response) => response);
  }
}
export default new UserService();
