import axios from 'axios';

export default {
    createUser(user) {
        axios.post("http://localhost:8000/users/", user).then(
            user => console.log(user)
        )
    }
}