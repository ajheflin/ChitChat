<template>
  <v-list-item
    v-if="contact"
    link
    class="py-4"
    :to="`/contact/${contact.id}`"
    :key="contact.id"
  >
    <Avatar :user="contact" />
    <v-list-item-content>
      <v-list-item-title>{{ contact.name }}</v-list-item-title>
      <v-list-item-subtitle>{{ contact.username }}</v-list-item-subtitle>
    </v-list-item-content>
  </v-list-item>
</template>
<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import { Prop } from "vue-property-decorator";
import IUser from "../interfaces/user.interface";
import Avatar from "./Avatar.vue";

@Component({
  components: { Avatar },
})
export default class ContactListItem extends Vue {
  @Prop() readonly contact: IUser | undefined;
}
</script>
