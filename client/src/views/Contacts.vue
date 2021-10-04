<template>
  <div>
    <h3 class="text-center mt-5">This is Contacts</h3>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import { MetaInfo } from "vue-meta";
import { ROUTES } from "../router/routes";
@Component({
  name: ROUTES.CONTACTS,
  metaInfo(): MetaInfo {
    return { title: `ChitChat - ${ROUTES.CONTACTS}` };
  },
})
export default class Contacts extends Vue {}
</script>
