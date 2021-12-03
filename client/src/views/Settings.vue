<<<<<<< HEAD
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
=======
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
>>>>>>> 2e59c4d072d617713f8689705bba8d7a5c9f14c6
