<template>
  <v-container>
    <ContactList />
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import { MetaInfo } from "vue-meta";
import { ROUTES } from "../router/routes";
import ContactList from "../components/ContactList.vue";
@Component<Contacts>({
  name: ROUTES.CONTACTS,
  metaInfo(): MetaInfo {
    return { title: `ChitChat - ${ROUTES.CONTACTS}` };
  },
  components: {
    ContactList,
  },
})
export default class Contacts extends Vue {}
</script>
