<template>
  <v-row fluid>
    <v-col cols="11" md="6" class="mx-auto">
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
import IChat from "../interfaces/chat.interface";
import IUser from "../interfaces/user.interface";
import IDivider from "../interfaces/divider.interface";
import { addDividers } from "../helpers/divider.helper";

@Component({ components: { ChatListItem } })
export default class ChatList extends Vue {
  private user: IUser = { id: "123", username: "johndoe", name: "John Doe" };
  private chats: (IChat | IDivider)[] = [
    {
      id: "o912u59qawaw5awfn",
      users: [
        { id: "123", username: "johndoe", name: "John Doe" },
        {
          id: "456",
          username: "sallyjones",
          name: "Sally Jones",
          profile_photo:
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQo4p7dS0kGOK3eRnM1W-mJtgc68uRYVGOtRg&usqp=CAU",
        },
      ],
      messages: [
        {
          id: "0wja3nga",
          sender: {
            id: "456",
            username: "sallyjones",
            name: "Sally Jones",
            profile_photo:
              "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQo4p7dS0kGOK3eRnM1W-mJtgc68uRYVGOtRg&usqp=CAU",
          },
          content: "Hello World!",
        },
      ],
    },
    {
      id: "o912u59awets3qawfn",
      users: [
        { id: "123", username: "johndoe", name: "John Doe" },
        {
          id: "456",
          username: "jackjones",
          name: "Jack Jones",
          profile_photo:
            "https://sunrift.com/wp-content/uploads/2014/12/Blake-profile-photo-square.jpg",
        },
      ],
      messages: [
        {
          id: "aiwnvaewg",
          sender: {
            id: "456",
            username: "jackjones",
            name: "Jack Jones",
            profile_photo:
              "https://sunrift.com/wp-content/uploads/2014/12/Blake-profile-photo-square.jpg",
          },
          content: "Hello World!",
        },
      ],
    },
  ];
  mounted() {
    this.chats = addDividers(this.chats);
  }
}
</script>
