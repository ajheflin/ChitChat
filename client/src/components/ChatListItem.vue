<template>
  <v-list-item
    v-if="chat && user"
    link
    :to="`/chat/${chat.id}`"
    class="py-4"
    :key="chat.id"
  >
    <v-avatar color="indigo" class="white--text mr-5">
      <v-img
        v-if="getChatter(chat.users).profile_photo"
        :src="getChatter(chat.users).profile_photo"
      />
      <span v-else>{{ getNameAbbrev(getChatter(chat.users).name) }}</span>
    </v-avatar>
    <v-list-item-content>
      <v-list-item-title
        v-html="getChatter(chat.users).name"
      ></v-list-item-title>
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

@Component({})
export default class ChatListItem extends Vue {
  @Prop() readonly chat: IChat | undefined;
  @Prop() readonly user: IUser | undefined;
  private getNameAndContent(msg: IMessage, chat: IChat) {
    const sender = chat.users.find((u) => u.id == msg.sender_id);
    return `<span class="font-weight-bold">${sender?.name}</span> — ${msg.content}`;
  }

  public getNameAbbrev(name: string) {
    const [first, last] = name.split(" ");
    return `${first[0]}${last[0]}`;
  }

  private getChatter(users: IUser[]) {
    return users.find((u) => u.id !== this.user?.id);
  }
}
</script>
