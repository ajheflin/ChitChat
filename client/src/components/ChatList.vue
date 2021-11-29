<template>
  <v-row v-if="chats.length > 0" fluid>
    <v-col cols="11" md="6" class="mx-auto">
      <v-list two-line>
        <template v-for="(chat, i) in chats">
          <v-divider v-if="chat.divider" :key="`${i}-divider`"></v-divider>
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
import { mapGetters } from "vuex";
import axios from "axios";

@Component({
  components: { ChatListItem },
  computed: { ...mapGetters(["AuthModule/getUser"]) },
})
export default class ChatList extends Vue {
  // private user: IUser = { id: "123", username: "johndoe", name: "John Doe" };
  private chats: (IChat | IDivider)[] = [];
  get user(): IUser {
    return this.$store.getters["AuthModule/getUser"];
  }
  async created() {
    try {
      const res = await axios.get(`/api/users/${this.user.id}/chats`);
      this.chats = res.data as IChat[];
    } catch (err) {
      console.error(err);
    }
    this.chats = addDividers(this.chats);
  }
}
</script>
