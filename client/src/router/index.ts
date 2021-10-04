import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";
import { ROUTES } from "./routes";
import Chats from "../views/Chats.vue";
import Chat from "../views/Chat.vue";
import Contacts from "../views/Contacts.vue";
import Settings from "../views/Settings.vue";
import Archive from "../views/Archive.vue";
import VueMeta from "vue-meta";

Vue.use(VueRouter);
Vue.use(VueMeta);

const lower = (route: string) => route.toLowerCase();

const routes: Array<RouteConfig> = [
  { path: "/", redirect: `/${lower(ROUTES.CHATS)}` },
  {
    path: `/${lower(ROUTES.ARCHIVE)}`,
    name: ROUTES.ARCHIVE,
    component: Archive,
  },
  {
    path: `/${lower(ROUTES.CHATS)}`,
    name: ROUTES.CHATS,
    component: Chats,
  },
  {
    path: `/${lower(ROUTES.CHAT)}/:id`,
    name: ROUTES.CHAT,
    component: Chat,
  },
  {
    path: `/${lower(ROUTES.CONTACTS)}`,
    name: ROUTES.CONTACTS,
    component: Contacts,
  },
  {
    path: `/${lower(ROUTES.SETTINGS)}`,
    name: ROUTES.SETTINGS,
    component: Settings,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
