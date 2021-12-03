import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";
import store from "@/store/index";
import { ROUTES } from "./routes";
const Chats = () => import("../views/Chats.vue");
const Chat = () => import("../views/Chat.vue");
const Contacts = () => import("../views/Contacts.vue");
const Settings = () => import("../views/Settings.vue");
const Archive = () => import("../views/Archive.vue");
const Profile = () => import("../views/Profile.vue");
const Login = () => import("../views/Login.vue");
const Signup = () => import("../views/Signup.vue");
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
    meta: { requiresAuth: true },
  },
  {
    path: `/${lower(ROUTES.CHATS)}`,
    name: ROUTES.CHATS,
    component: Chats,
    meta: { requiresAuth: true },
  },
  {
    path: `/${lower(ROUTES.CHAT)}/:id`,
    name: ROUTES.CHAT,
    component: Chat,
    meta: { requiresAuth: true },
  },
  {
    path: `/${lower(ROUTES.PROFILE)}/:id`,
    name: ROUTES.PROFILE,
    component: Profile,
    meta: { requiresAuth: true },
  },
  {
    path: `/${lower(ROUTES.CONTACTS)}`,
    name: ROUTES.CONTACTS,
    component: Contacts,
    meta: { requiresAuth: true },
  },
  {
    path: `/${lower(ROUTES.SETTINGS)}`,
    name: ROUTES.SETTINGS,
    component: Settings,
    meta: { requiresAuth: true },
  },
  {
    path: `/${lower(ROUTES.LOGIN)}`,
    name: ROUTES.LOGIN,
    component: Login,
    meta: { requiresAuth: false },
  },
  {
    path: `/${lower(ROUTES.SIGNUP)}`,
    name: ROUTES.SIGNUP,
    component: Signup,
    meta: { requiresAuth: false },
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach(async (to, from, next) => {
  const isLoggedIn = store.getters["AuthModule/isLoggedIn"];
  if (to.matched.some((record) => record.meta.isGuestRoute)) {
    if (isLoggedIn) return next({ path: `/${lower(ROUTES.CHATS)}` });
    next();
  } else if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (!isLoggedIn) {
      next({ path: "/login", query: { redirect: to.fullPath } });
    }
    next();
  }
  next();
});

export default router;
