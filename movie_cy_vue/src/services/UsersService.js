import axios from "axios";

export default {
  createUser(user) {
    console.log(user);
    axios
      .post("http://localhost:8000/users/", user)
      .then((user) => user);
  },

  isUserExist(user) {
    return axios.post("http://localhost:8000/users/", user)
  }
};
