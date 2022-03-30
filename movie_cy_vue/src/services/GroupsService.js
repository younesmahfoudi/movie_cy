import axios from "axios";

const API_URL = "http://localhost:8000/groups/";

class GroupService {
  createGroup(token, group) {
    console.log(group);
    axios
      .post(API_URL, group, {
        headers: {
          Authorization: `Bearer ${token.access_token}`,
        },
      })
      .then((group) => group);
  }

  getGroup(token, id) {
    return axios
      .get(API_URL + id, {
        headers: {
          Authorization: `Bearer ${token.access_token}`,
        },
      })
      .then((response) => {
        return response.data.items;
      });
  }

  updateGroup(token, id, data) {
    return axios
      .put(API_URL + id, data, {
        headers: {
          Authorization: `Bearer ${token.access_token}`,
        },
      })
      .then((response) => {
        return response;
      });
  }

  deleteUser(token, id) {
    return axios
      .delete(API_URL + id, {
        headers: {
          Authorization: `Bearer ${token.access_token}`,
        },
      })
      .then((response) => {
        return response;
      });
  }
}
export default new GroupService();
