<template>
  <section class="chat text-center mt-5 text-h6">
    This is user profile of user with id: {{ this.$route.params.id }}
  </section>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import { ROUTES } from "../router/routes";
import { MetaInfo } from "vue-meta";

@Component<Profile>({
  metaInfo(): MetaInfo {
    return {
      title: `ChitChat - ${ROUTES.PROFILE} of ${this.$route.params.id}`,
    };
  }, //replace id with chatter username

  name: ROUTES.PROFILE,
})
export default class Profile extends Vue {}
</script>
