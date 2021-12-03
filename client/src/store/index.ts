import Vue from "vue";
import Vuex from "vuex";
import { AuthModule } from "./auth.module";
import VuexPersistence from "vuex-persist";

Vue.use(Vuex);

const vuexLocal = new VuexPersistence({
  storage: window.sessionStorage,
  key: "vuex",
});

export default new Vuex.Store({
  modules: { AuthModule },
  plugins: [vuexLocal.plugin],
});
