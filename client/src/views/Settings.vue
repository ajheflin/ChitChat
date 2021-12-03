<template>
  <SettingsOptions />
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import { MetaInfo } from "vue-meta";
import { ROUTES } from "../router/routes";
import SettingsOptions from "../components/SettingsOptions.vue";
@Component<Settings>({
  name: ROUTES.SETTINGS,
  components: { SettingsOptions },
  metaInfo(): MetaInfo {
    return { title: `ChitChat - ${ROUTES.SETTINGS}` };
  },
})
export default class Settings extends Vue {}
</script>
