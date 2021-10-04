<template>
  <v-row fluid>
    <v-col cols="12" sm="6" offset-sm="3">
      <v-list two-line>
        <template v-for="(chat, i) in chats">
          <v-divider v-if="chat.divider" :key="i"></v-divider>
          <v-list-item
            link
            :to="`/chat/${chat.id}`"
            class="py-4"
            v-else
            :key="chat.id"
          >
            <v-avatar color="indigo" class="white--text mr-5">
              <v-img
                v-if="getChatter(chat.users).profile_photo"
                :src="getChatter(chat.users).profile_photo"
              />
              <span v-else>{{
                getNameAbbrev(chat.users.find((u) => u.id !== user.id).name)
              }}</span>
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
      </v-list>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import { ROUTES } from "../router/routes";
import { MetaInfo } from "vue-meta";
import IChat from "../interfaces/chat.interface";
import IUser from "../interfaces/user.interface";
import IMessage from "../interfaces/chat-message.interface";

@Component<Chats>({
  metaInfo(): MetaInfo {
    return { title: `ChitChat - ${ROUTES.CHATS}` };
  },
  name: ROUTES.CHATS,
})
export default class Chats extends Vue {
  private user: IUser = { id: "123", username: "johndoe", name: "John Doe" };

  private chats: IChat[] = [
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
    return this.chats.flatMap((val, i, arr) =>
      arr.length - 1 !== i // check for the last item
        ? [val, { divider: true }]
        : val
    );
  }

  private getChatter(users: IUser[]) {
    return users.find((u) => u.id !== this.user.id);
  }

  private getNameAndContent(msg: IMessage, chat: IChat) {
    const sender = chat.users.find((u) => u.id == msg.sender_id);
    return `<span class="font-weight-bold">${sender.name}</span> — ${msg.content}`;
  }

  public getNameAbbrev(name: string) {
    const [first, last] = name.split(" ");
    return `${first[0]}${last[0]}`;
  }
}
</script>
