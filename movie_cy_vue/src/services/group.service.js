import api from "./api";

class GroupService {
  getGroups(groupId) {
    return api
      .get(`/groups/${groupId}`)
      .then((response) => response.data.data[0]);
  }
}

export default new GroupService();
