import axios from "axios";
import authHeader from "./auth-headers";

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
        return response.data[0];
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

  updateGroupById(group) {
    return axios
      .put(API_URL + group.id, group, {
        headers: authHeader(),
      })
      .then((response) => {
        return response;
      });
  }

  getGroupById(id) {
    return axios.get(API_URL + id, authHeader()).then((response) => {
      return response.data.data[0];
    });
  }

  deleteUserFromGroups(user) {
    const groups = user.groups;
    for (let groupID in groups) {
      let group = this.getGroupById(groupID);
      group.membres = this.deleteUserFromList(user, group);
      this.updateGroupById(group);
    }
  }

  deleteUserFromList(user, list) {
    for (var i = 0; i < list.length; i++) {
      if (list[i] === user.id) {
        list.splice(i, 1);
      }
    }
    return list;
  }
}
export default new GroupsService();
