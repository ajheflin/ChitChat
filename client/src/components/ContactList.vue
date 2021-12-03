<template>
  <v-row fluid>
    <v-col cols="11" md="6" class="mx-auto">
      <v-list two-line>
        <!-- <template v-for="(contact, i) in contacts">
          <v-divider v-if="contact.divider" :key="i"></v-divider>
          <ContactListItem v-else :key="contact.id" :contact="contact" />
        </template> -->
      </v-list>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import IUser from "../interfaces/user.interface";
import ContactListItem from "./ContactListItem.vue";
import { addDividers } from "../helpers/divider.helper";
import IDivider from "../interfaces/divider.interface";

@Component({ components: { ContactListItem } })
export default class ChatList extends Vue {
  // private user: IUser = { id: "123", username: "johndoe", name: "John Doe" };
  // private contacts: (IUser | IDivider)[] = [
  //   {
  //     id: "pneu2h35",
  //     name: "Sally Jones",
  //     username: "sj56",
  //   },
  // ];
  // mounted() {
  //   this.contacts = addDividers(this.contacts);
  // }
}
</script>
