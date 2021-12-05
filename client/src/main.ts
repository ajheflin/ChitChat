import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import VueMeta from "vue-meta";
import VueSocketIO from "vue-socket.io";
import "./index.css";
import VueNativeSock from "vue-native-websocket";
Vue.config.productionTip = false;

Vue.use(VueNativeSock, "ws://localhost:8000/api/chat", {
  connectManually: true,
});
Vue.use(VueMeta, { keyName: "head" });
// Vue.use(
//   new VueSocketIO({
//     debug: true,
//     connection: "ws://localhost:8000",
//   })
// );

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
