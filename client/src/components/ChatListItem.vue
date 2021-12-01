<template>
  <v-list-item
    v-if="loaded"
    link
    :to="`/chat/${chat.id}`"
    class="py-4"
    :key="chat.id"
  >
    <Avatar :image="avatar" />
    <v-list-item-content>
      <v-list-item-title>{{ title }}</v-list-item-title>
      <v-list-item-subtitle v-html="subtitle">{{}}</v-list-item-subtitle>
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
  @Prop() readonly users: IUser[] | undefined;
  private messages: IMessage[] = [];
  private loaded = false;

  get avatar() {
    if (this.chat.users.length === 1) return this.user.avatar_url;
    if (this.chat.users.length === 2)
      return this.users.find((u) => u.id !== this.user.id).avatar_url;
    return this.chat.chat_image;
  }

  get title() {
    console.log(this.chat);
    if (this.chat.users.length === 1) return this.user.name;
    if (this.chat.users.length === 2)
      this.users.find((u) => u.id !== this.user.id).name;
    return this.chat.name;
  }

  public get subtitle() {
    if (this.messages.length <= 0)
      return `<span class="font-weight-bold">No messages in chat</span>`;
    const lastMsg = this.messages[this.messages.length - 1];
    const senderOfLastMsg = this.users.find((u) => u.id === lastMsg.sender);
    return `<span class="font-weight-bold">${senderOfLastMsg.name}</span> — ${lastMsg.content}`;
  }

  private async created() {
    const res = await axios.get<IMessage[]>(
      `/api/messages/chat/${this.chat.id}`
    );
    this.messages = res.data;
    this.loaded = true;
  }
}
</script>
