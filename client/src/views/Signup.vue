<template>
  <div><h3 class="text-center mt-5">This is Signup</h3></div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import { MetaInfo } from "vue-meta";
import { ROUTES } from "../router/routes";

@Component<Signup>({
  name: ROUTES.SIGNUP,
  metaInfo(): MetaInfo {
    return { title: `ChitChat - ${ROUTES.SIGNUP}` };
  },
})
export default class Signup extends Vue {}
</script>
