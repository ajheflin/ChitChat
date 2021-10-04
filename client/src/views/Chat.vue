<template>
  <section class="chat text-center mt-5 text-h6">
    This is chat with id: {{ this.$route.params.id }}
  </section>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import { ROUTES } from "../router/routes";
import { MetaInfo } from "vue-meta";
import ChatList from "../components/ChatList.vue";

@Component<Chats>({
  metaInfo(): MetaInfo {
    return { title: `ChitChat - ${ROUTES.CHAT} with ${this.$route.params.id}` };
  }, //replace id with chatter username
  components: { ChatList },
  name: ROUTES.CHATS,
})
export default class Chats extends Vue {}
</script>
