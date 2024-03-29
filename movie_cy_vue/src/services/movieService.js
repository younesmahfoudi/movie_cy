import axios from "axios";

class MovieService {
  async getMovies(token, url,page, limit) {
    return axios
      .get(`${url}&page=${page}&size=${limit}`, {
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
