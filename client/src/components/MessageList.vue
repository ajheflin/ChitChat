<template>
  <v-row v-if="loaded" fluid class="relative">
    <v-col>
      <v-list ref="msgList" class="h-fit overflow-y-scroll" two-line>
        <template v-for="(message, i) in messages">
          <MessageListItem
            :key="i"
            :user="user"
            :users="users"
            :message="message"
          />
        </template>
      </v-list>
      <v-form>
        <v-text-field
          class="sticky w-full h-16 px-5 ml-auto"
          v-model="message"
          append-outer-icon="mdi-send"
          filled
          clearable
          clear-icon="mdi-close-circle"
          label="Message"
          type="text"
          @click:append-outer="sendMsg"
          @keypress.enter="sendMsg"
          @click:clear="clearMessage"
        ></v-text-field>
      </v-form>
    </v-col>
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
import IMessage from "../interfaces/message.interface";
import IUser from "../interfaces/user.interface";
import MessageListItem from "./MessageListItem.vue";
import axios from "axios";
import { Watch } from "vue-property-decorator";

@Component({ components: { MessageListItem } })
export default class MessageList extends Vue {
  @Watch("messages")
  async onMessagesChanged() {
    await this.$nextTick();
    this.scrollToLatestMsg();
  }
  private messages: IMessage[] = [];
  private users: IUser[] = [];
  private message = "";
  private loaded = false;
  private WS_URL = `ws://3.15.140.219:8000/api/ws/chat/${
    (this as any).$route.params.id
  }`;

  public async mounted() {
    const [resMessages, resUsers] = await Promise.all([
      axios.get<IMessage[]>(
        `/api/messages/chat/${(this as any).$route.params.id}`
      ),
      axios.get<IUser[]>(`/api/users`),
    ]);
    this.messages = resMessages.data;
    this.users = resUsers.data;
    this.loaded = true;
    (this as any).$connect(this.WS_URL, {
      format: "json",
    });
    (this.$options as any).sockets.onmessage = this.onMessage;
    await this.$nextTick();
    document.documentElement.style.overflowY = "hidden";
    this.scrollToLatestMsg();
  }

  public onMessage(msg: MessageEvent) {
    const data = JSON.parse(msg.data) as IMessage;
    if (data.sender !== this.user.id) return this.messages.push(data);
  }

  public destroyed() {
    (this as any).$disconnect();
    delete (this.$options as any).sockets.onmessage;
    document.documentElement.style.overflowY = "auto";
  }

  public async sendMsg(e: Event) {
    e.preventDefault();
    const data = {
      sender: this.user.id,
      content: this.message,
      chat: (this as any).$route.params.id,
    };
    this.messages.push({
      ...data,
      last_modified: new Date(),
      created: new Date(),
    });
    (this as any).$socket.send(JSON.stringify(data));
    this.message = "";
    await this.$nextTick();
    this.scrollToLatestMsg();
  }

  private scrollToLatestMsg() {
    const msgList = (this?.$refs?.msgList as Vue)?.$el;
    msgList.scrollTop = msgList.scrollHeight;
  }

  public clearMessage() {
    this.message = "";
  }

  get user(): IUser {
    return this["$store"].getters["AuthModule/getUser"];
  }
}
</script>

<style lang="scss">
.h-fit {
  height: calc(100vh - 150px);
}
.v-list-item__content {
  display: flex !important;
  justify-items: flex-end !important;
  flex: initial !important;
}
</style>
