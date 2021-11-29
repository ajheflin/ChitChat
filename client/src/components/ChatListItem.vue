<template>
  <v-list-item
    v-if="!!chat && !!user && !!messages && !!sender && !!chatter"
    link
    :to="`/chat/${chat.id}`"
    class="py-4"
    :key="chat.id"
  >
    <Avatar :user="chatter" />
    <v-list-item-content>
      <v-list-item-title>{{ chatter.name }}</v-list-item-title>
      <v-list-item-subtitle
        v-html="getNameAndContent"
        >{{
      }}</v-list-item-subtitle>
    </v-list-item-content>
  </v-list-item>
</template>
<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import IChat from "../interfaces/chat.interface";
import { Prop } from "vue-property-decorator";
import IUser from "../interfaces/user.interface";
import IMessage from "../interfaces/message.interface";
import Avatar from "./Avatar.vue";
import axios from "axios";

@Component({
  components: { Avatar },
})
export default class ChatListItem extends Vue {
  @Prop() readonly chat: IChat | undefined;
  @Prop() readonly user: IUser | undefined;
  private messages: IMessage[] = [];
  private sender: IUser | null = null;
  private chatter: IUser | null = null;

  get getNameAndContent() {
    return `<span class="font-weight-bold">${this.sender?.name}</span> — ${
      this?.messages.at(-1).content
    }`;
  }

  private async created() {
    const messages: IMessage[] = (
      await axios.get(`/api/messages/chat/${this.chat.id}`)
    ).data;
    this.messages = messages;
    if (this.messages.length > 0) {
      const sender = (
        await axios.get(`/api/users/${this?.messages.at(-1).sender}`)
      ).data[0];
      this.sender = sender;
      const chatterId = this.chat.users.find((id) => id !== this?.user.id);
      if (this?.sender.id === chatterId) this.chatter = sender;
      else this.chatter = this.user;
    }
  }
}
</script>
