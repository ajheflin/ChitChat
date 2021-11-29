<template>
  <v-row fluid class="relative">
    <v-col>
      <v-list ref="msgList" class="h-80vh overflow-y-scroll" two-line>
        <template v-for="message in messages">
          <MessageListItem :key="message.id" :user="user" :message="message" />
        </template>
      </v-list>
      <v-form>
        <v-text-field
          class="sticky w-full px-3 lg:px-5 ml-auto"
          v-model="message"
          append-outer-icon="mdi-send"
          filled
          clear-icon="mdi-close-circle"
          clearable
          label="Message"
          type="text"
          @click:append-outer="sendMsg"
        ></v-text-field>
      </v-form>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import IMessage from "../interfaces/message.interface";
import IUser from "../interfaces/user.interface";
import MessageListItem from "./MessageListItem.vue";
import axios from "axios";
import { Watch } from "vue-property-decorator";

@Component({ components: { MessageListItem } })
export default class MessageList extends Vue {
  public message = "";
  private messages: IMessage[] = [];
  get user(): IUser {
    return this.$store.getters["AuthModule/getUser"];
  }
  public async sendMsg() {
    const res = await axios.post("/api/messages/manage", {
      sender: this.user.id,
      chat: this.$route.params.id,
      content: this.message,
    });
    const msg: IMessage = res.data;
    this.messages.push(msg);
    await this.$nextTick();
    this.scrollToLatestMsg();
  }

  scrollToLatestMsg() {
    const msgList = this.$refs.msgList.$el;
    msgList.scrollTop = msgList.scrollHeight - msgList.clientHeight;
  }

  async created() {
    const messages = (
      await axios.get(`/api/messages/chat/${this.$route.params.id}`)
    ).data;
    this.messages = messages;
    document.documentElement.style.overflowY = "hidden";
  }
  destroyed() {
    document.documentElement.style.overflowY = "auto";
  }
}
</script>

<style lang="scss">
.h-80vh {
  height: 80vh;
}
.v-list-item__content {
  display: flex !important;
  justify-items: flex-end !important;
  flex: initial !important;
}
</style>
