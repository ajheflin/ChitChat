<template>
  <v-list-item
    v-if="chat && user"
    link
    :to="`/chat/${chat.id}`"
    class="py-4"
    :key="chat.id"
  >
    <Avatar :user="getChatter(chat.users)" />
    <v-list-item-content>
      <v-list-item-title>{{ getChatter(chat.users).name }}</v-list-item-title>
      <v-list-item-subtitle
        v-html="getNameAndContent(chat.messages.at(-1), chat)"
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
import IMessage from "../interfaces/chat-message.interface";
import Avatar from "./Avatar.vue";

@Component({
  components: { Avatar },
})
export default class ChatListItem extends Vue {
  @Prop() readonly chat: IChat | undefined;
  @Prop() readonly user: IUser | undefined;

  private getNameAndContent(msg: IMessage, chat: IChat) {
    const sender = chat.users.find((u) => u.id == msg.sender_id);
    return `<span class="font-weight-bold">${sender?.name}</span> — ${msg.content}`;
  }

  private getChatter(users: IUser[]) {
    return users.find((u) => u.id !== this.user?.id);
  }
}
</script>
