<template>
  <div><h3 class="text-center mt-5">This is Archive</h3></div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import { MetaInfo } from "vue-meta";
import { ROUTES } from "../router/routes";

@Component<Archive>({
  name: ROUTES.ARCHIVE,
  metaInfo(): MetaInfo {
    return { title: `ChitChat - ${ROUTES.ARCHIVE}` };
  },
})
export default class Archive extends Vue {}
</script>
