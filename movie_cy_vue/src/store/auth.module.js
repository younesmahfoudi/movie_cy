import AuthService from "../services/auth.service";
const user = JSON.parse(localStorage.getItem("user"));
const initialState = user
  ? { status: { loggedIn: true }, user }
  : { status: { loggedIn: false }, user: null };
export const auth = {
  namespaced: true,
  state: initialState,
  actions: {
    login({ commit }, user) {
      return AuthService.login(user).then((data) => {
        if (data.access_token) {
          commit("loginSuccess", data);
          return Promise.resolve(user);
        } else {
          commit("loginFailure");
          return Promise.reject(data);
        }
      });
    },
    logout({ commit }) {
      AuthService.logout();
      commit("logout");
    },
    register({ commit }, user) {
      return AuthService.register(user).then((data) => {
        if (data.access_token) {
          commit("registerSuccess", data);
          return Promise.resolve(user);
        } else {
          commit("registerFailure");
          return Promise.reject(data);
        }
      });
    },
  },
  mutations: {
    loginSuccess(state, user) {
      state.status.loggedIn = true;
      state.user = user;
    },
    loginFailure(state) {
      state.status.loggedIn = false;
      state.user = null;
    },
    logout(state) {
      state.status.loggedIn = false;
      state.user = null;
    },
    registerSuccess(state, user) {
      state.status.loggedIn = false;
      state.user = user;
    },
    registerFailure(state) {
      state.status.loggedIn = false;
    },
  },
};
