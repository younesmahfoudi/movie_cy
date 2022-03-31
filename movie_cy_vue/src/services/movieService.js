import axios from "axios";

class MovieService {
  async getMovies(token, url, limit) {
    console.log(`${url}&page=1&size=${limit}`);
    return axios
      .get(`${url}&page=1&size=${limit}`, {
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
