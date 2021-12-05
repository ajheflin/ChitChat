<template>
  <LoginForm />
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import { MetaInfo } from "vue-meta";
import { ROUTES } from "../router/routes";
import LoginForm from "../components/LoginForm.vue";

@Component<Login>({
  name: ROUTES.LOGIN,
  components: { LoginForm },
  metaInfo(): MetaInfo {
    return { title: `ChitChat - ${ROUTES.LOGIN}` };
  },
})
export default class Login extends Vue {}
</script>
