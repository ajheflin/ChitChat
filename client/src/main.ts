import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import VueMeta from "vue-meta";
import "./index.css";
import VueNativeSock from "vue-native-websocket";
Vue.config.productionTip = false;

Vue.use(VueNativeSock as any, "/api/ws/", {
  connectManually: true,
  reconnect: true,
  reconnectionDelay: 1000,
});
Vue.use(VueMeta, { keyName: "head" });

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
