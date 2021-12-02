<template>
  <SignupForm />
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import { MetaInfo } from "vue-meta";
import { ROUTES } from "../router/routes";
import SignupForm from "../components/SignupForm.vue";

@Component<Signup>({
  name: ROUTES.SIGNUP,
  components: { SignupForm },
  metaInfo(): MetaInfo {
    return { title: `ChitChat - ${ROUTES.SIGNUP}` };
  },
})
export default class Signup extends Vue {}
</script>
