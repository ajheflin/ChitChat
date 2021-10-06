<template>
  <v-container class="chats"><ChatList /></v-container>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import { ROUTES } from "../router/routes";
import { MetaInfo } from "vue-meta";
import ChatList from "../components/ChatList.vue";

@Component<Chats>({
  metaInfo(): MetaInfo {
    return { title: `ChitChat - ${ROUTES.CHATS}` };
  },
  components: { ChatList },
  name: ROUTES.CHATS,
})
export default class Chats extends Vue {}
</script>
