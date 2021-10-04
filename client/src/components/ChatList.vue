<template>
  <v-row fluid>
    <v-col cols="12" sm="6" offset-sm="3">
      <v-list two-line>
        <template v-for="(chat, i) in chats">
          <v-divider v-if="chat.divider" :key="i"></v-divider>
          <ChatListItem v-else :key="chat.id" :chat="chat" :user="user" />
        </template>
      </v-list>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import ChatListItem from "./ChatListItem.vue";
import IMessage from "../interfaces/chat-message.interface";
import IChat from "../interfaces/chat.interface";
import IUser from "../interfaces/user.interface";

interface IDivider {
  divider: boolean;
}

@Component({ components: { ChatListItem } })
export default class ChatList extends Vue {
  private user: IUser = { id: "123", username: "johndoe", name: "John Doe" };
  private chats: (IChat | IDivider)[] = [
    {
      id: "o912u59qawaw5awfn",
      users: [
        { id: "123", username: "johndoe", name: "John Doe" },
        { id: "456", username: "sallyjones", name: "Sally Jones" },
      ],
      messages: [
        {
          sender_id: "123",
          content: "Hello World!",
        },
      ],
    },
    {
      id: "o912u59awets3qawfn",
      users: [
        { id: "123", username: "johndoe", name: "John Doe" },
        { id: "456", username: "jackjones", name: "Jack Jones" },
      ],
      messages: [
        {
          sender_id: "123",
          content: "Hello World!",
        },
      ],
    },
  ];
  mounted() {
    this.chats = this.addDividers();
  }
  private addDividers() {
    return this.chats.flatMap(
      (val: IChat | IDivider, i: number, arr: (IChat | IDivider)[]) =>
        arr.length - 1 !== i // check for the last item
          ? [val, { divider: true }]
          : val
    );
  }
}
</script>
