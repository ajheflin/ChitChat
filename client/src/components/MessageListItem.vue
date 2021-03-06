<template>
  <v-list-item
    v-if="message && user && users"
    class="py-4 w-full md:w-3/4 lg:w-1/2"
    :class="{
      'ml-auto': senderIsCurUser(),
    }"
    :key="message.id"
  >
    <Avatar :user="message.sender.avatar" />
    <v-list-item-content
      :class="{
        'ml-auto': senderIsCurUser(),
      }"
    >
      <v-list-item-title
        class="mb-3 text-gray-500 text-sm"
        :class="{
          'text-right': senderIsCurUser(),
          'text-left': !senderIsCurUser(),
        }"
        >{{ sender.username }}</v-list-item-title
      >
      <v-list-item-subtitle
        class="pa-4 rounded-lg overflow whitespace-normal"
        :class="{
          'text-right text-white': senderIsCurUser(),
          'text-left text-black': !senderIsCurUser(),
        }"
        :style="bubbleStyleObj"
        >{{ message.content }}</v-list-item-subtitle
      >
    </v-list-item-content>
  </v-list-item>
</template>
<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import { Prop } from "vue-property-decorator";
import IUser from "../interfaces/user.interface";
import IMessage from "../interfaces/message.interface";
import Avatar from "./Avatar.vue";

@Component({
  components: { Avatar },
})
export default class MessageListItem extends Vue {
  @Prop() readonly message: IMessage | undefined;
  @Prop() readonly user: IUser | undefined;
  @Prop() readonly users: IUser[] | undefined;

  private get sender() {
    return this?.users?.find((u) => u.id === this?.message?.sender);
  }

  private senderIsCurUser() {
    return this.message?.sender === this.user?.id;
  }

  get bubbleStyleObj(): { backgroundColor: string } {
    const isCurUser = this.senderIsCurUser();
    return { backgroundColor: isCurUser ? "#11a5ed" : "#e4eaf1" };
  }
}
</script>
