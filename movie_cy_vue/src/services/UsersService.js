import axios from 'axios';

export default {
    createUser(user) {
        axios.post("http://localhost:8000/users/", {
            "nom": "John Doe",
            "prenom": "John Doe",
            "email": "jdoe@x.edu.ng",
            "mdp": "exampleMDP",
            "films": [
                "film",
                "film2"
            ],
            "groupes": [
                "groupe",
                "groupe1"
            ],
            "mood": "fun",
            "acteur": "exampleIDAuteur",
            "realisateur": "exampleIDRealisateur",
            "genre": "comedie",
            "genreFlex": "comedie",
            "ddn": "2022-03-23",
            "age": 20,
            "avatar": "avatar",

        }).then(
            user => console.log(user)
        )
    }
}