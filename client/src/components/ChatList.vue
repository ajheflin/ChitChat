<template>
  <v-row v-if="loaded" fluid>
    <v-col cols="11" md="6" class="mx-auto">
      <v-list two-line>
        <template v-for="(chat, i) in chats">
          <v-divider v-if="chat.divider" :key="`${i}-divider`"></v-divider>
          <ChatListItem v-else :key="chat.id" :chat="chat" :user="user" />
        </template>
      </v-list>
    </v-col>
    <v-btn
      fab
      color="primary"
      class="mb-14 mr-5"
      bottom
      right
      absolute
      @click="dialog = !dialog"
    >
      <v-icon>mdi-plus</v-icon>
    </v-btn>
    <v-dialog v-model="dialog">
      <v-card>
        <v-card-title>Create new chat</v-card-title>
        <v-card-text>
          <v-text-field v-model="newChat.name" label="Chat name"></v-text-field>
          <v-select
            v-model="newChat.user"
            :items="users.map((u) => u.username)"
            label="Select users"
            return-object
            single-line
          ></v-select>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text color="primary" @click="createNewChat">Create</v-btn
          ><v-btn text color="primary" @click="dialog = false">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
  <div v-else class="w-full flex justify-center mt-7">
    <v-progress-circular
      :size="50"
      class="mx-auto"
      color="primary"
      indeterminate
    ></v-progress-circular>
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
  private newChat = { name: "", user: null };
  private users: IUser[] = [];

  get user(): IUser {
    return this.$store.getters["AuthModule/getUser"];
  }

  async createNewChat() {
    const res = await axios.post(`/api/chats/manage`, {
      name: this.newChat.name,
      users: [
        this.users.find((u) => u.username === this.newChat.user)?.id,
        this.user.id,
      ],
    });
    const data = res.data;
    console.log(data);
    this.dialog = false;
  }

  async created() {
    try {
      const [chatsRes, usersRes] = await Promise.all([
        axios.get(`/api/users/${this.user.id}/chats`),
        axios.get(`/api/users`),
      ]);
      this.users = usersRes.data as IUser[];
      this.chats = chatsRes.data as IChat[];
      console.log(this.chats);
      this.chats = addDividers(this.chats);
      this.loaded = true;
    } catch (err) {
      console.error(err);
    }
  }
}
</script>
