<template>
  <div>
    <v-row v-if="loaded && chats.length > 0" fluid>
      <v-col cols="11" md="6" class="mx-auto">
        <v-list two-line>
          <template v-for="(chat, i) in chats">
            <v-divider v-if="chat.divider" :key="`${i}-divider`"></v-divider>
            <ChatListItem
              v-else
              :key="chat.id"
              :chat="chat"
              :user="user"
              :users="users"
            />
          </template>
        </v-list>
      </v-col>
    </v-row>
    <div
      v-else-if="loaded && chats.length <= 0"
      class="w-full flex justify-center mt-7 text-lg text-center md:text-xl text-gray-500"
    >
      You have no chats, press the plus button on the bottom right to get
      chatting!
    </div>
    <div v-else class="w-full flex justify-center mt-7">
      <v-progress-circular
        :size="50"
        class="mx-auto"
        color="primary"
        indeterminate
      ></v-progress-circular>
    </div>
    <v-btn
      fab
      color="primary"
      class="mb-12 mr-1"
      bottom
      right
      absolute
      @click="dialog = !dialog"
    >
      <v-icon>mdi-plus</v-icon>
    </v-btn>
    <v-dialog v-model="dialog" width="400">
      <v-card>
        <v-card-title>Create a New Chat</v-card-title>
        <v-card-text>
          <v-text-field v-model="newChat.name" label="Chat name"></v-text-field>
          <v-select
            v-model="newChat.users"
            :items="
              users.filter((u) => u.id !== user.id).map((u) => u.username)
            "
            label="Select users"
            multiple
            chips
            hint="Select users to be included in the chat"
            persistent-hint
          ></v-select>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text color="primary" @click="createNewChat">Create</v-btn
          ><v-btn text color="primary" @click="dialog = false">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import ChatListItem from "./ChatListItem.vue";
import IChat from "../interfaces/chat.interface";
import IUser from "../interfaces/user.interface";
import IDivider from "../interfaces/divider.interface";
import { addDividers } from "../helpers/divider.helper";
import axios from "axios";

@Component({
  components: { ChatListItem },
})
export default class ChatList extends Vue {
  private chats: (IChat | IDivider)[] = [];
  private loaded = false;
  private dialog = false;
  private newChat = { name: "", users: [] };
  private users: IUser[] = [];

  get user(): IUser {
    return this.$store.getters["AuthModule/getUser"];
  }

  async createNewChat() {
    const userIds = this.newChat.users.map(
      (username) => this?.users?.find((user) => user.username === username)?.id
    );
    const res = await axios.post(`/api/chats/manage`, {
      name: this.newChat.name,
      users: [...userIds, this.user.id],
      chat_image: "https://cdn-icons-png.flaticon.com/512/134/134914.png",
    });
    const data = res.data;
    this.chats.unshift(data);
    this.dialog = false;
    this.newChat = { name: "", users: [] };
  }

  async created() {
    try {
      const [chatsRes, usersRes] = await Promise.all([
        axios.get(`/api/users/${this.user.id}/chats`),
        axios.get(`/api/users`),
      ]);
      chatsRes.data = chatsRes.data.sort((a, b) => b.id - a.id);
      this.users = usersRes.data as IUser[];
      this.chats = addDividers(chatsRes.data as IChat[]);
      this.loaded = true;
    } catch (err) {
      console.error(err);
    }
  }
}
</script>
