<template>
  <div><h3 class="text-center mt-5">This is Settings</h3></div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import { MetaInfo } from "vue-meta";
import { ROUTES } from "../router/routes";
@Component<Settings>({
  name: ROUTES.SETTINGS,
  metaInfo(): MetaInfo {
    return { title: `ChitChat - ${ROUTES.SETTINGS}` };
  },
})
export default class Settings extends Vue {}
</script>
