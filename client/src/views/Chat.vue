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
import IUser from "../interfaces/user.interface";

@Component<Chat>({
  components: { MessageList },
  metaInfo(): MetaInfo {
    return { title: `ChitChat - ${ROUTES.CHAT} with ${this.username}` };
  }, //replace id with chatter username
  name: ROUTES.CHAT,
})
export default class Chat extends Vue {
  private username = "";
  async created() {
    const res = await axios.get(`/api/users/${this.$route.params.id}/`);
    this.username = (res.data as IUser).username;
  }
}
</script>
