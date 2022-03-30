import axios from "axios";

class MovieService {
  getMovies(token) {
    let url = "http://localhost:8000/movies/";

    return axios
      .get(url, {
        headers: {
          Authorization: `Bearer ${token.access_token}`,
        },
      })
      .then((response) => {
        response.data.items.forEach((e) => {
          e.genreList.forEach((element) => {
            element.value = `./src/components/icon/ThemeIcon/${element.value.toLowerCase()}.png`;
          });
        });
        return response.data.items;
      });
  }
}
export default new MovieService();
