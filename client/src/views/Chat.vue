<template>
  <section class="chat text-center mt-5 text-h6">
    <MessageList />
  </section>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import MessageList from "../components/MessageList.vue";
import { ROUTES } from "../router/routes";
import { MetaInfo } from "vue-meta";
import axios from "axios";
import IChat from "../interfaces/chat.interface";

@Component<Chat>({
  components: { MessageList },
  metaInfo(): MetaInfo {
    return { title: `ChitChat - ${this.chatName}` };
  },
  name: ROUTES.CHAT,
})
export default class Chat extends Vue {
  private chatName = "";
  async created() {
    const res = await axios.get(`/api/chats/${this.$route.params.id}/`);
    this.chatName = (res.data as IChat).name;
  }
}
</script>
