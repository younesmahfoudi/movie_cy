import axios from "axios";

export default {
  createGroup(group) {
    console.log(group);
    axios.post("http://localhost:8000/groups/", group).then((group) => group);
  },
};
