import axios from "axios";

const API_URL = "http://localhost:8000/groups/";

class GroupsService {
  createGroup(token, group) {
    return axios
      .post(API_URL, group, {
        headers: {
          Authorization: `Bearer ${token.access_token}`,
        },
      })
      .then((group) => {
        return group;
      });
  }

  getGroup(token, id) {
    return axios
      .get(API_URL + id, {
        headers: {
          Authorization: `Bearer ${token.access_token}`,
        },
      })
      .then((response) => {
        return response.data.data[0];
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
export default new GroupsService();
