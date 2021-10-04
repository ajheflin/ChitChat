<template>
  <nav>
    <v-app-bar app color="primary pr-2" absolute flat>
      <v-app-bar-nav-icon dark @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-spacer></v-spacer>
      <v-btn dark icon>
        <v-icon>mdi-bell</v-icon>
      </v-btn>
      <v-btn dark icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-app-bar>
    <v-navigation-drawer v-model="drawer" absolute temporary>
      <v-list class="mt-2">
        <v-list-item>
          <v-avatar color="purple" icon class="mb-2"
            ><span class="white--text">JD</span></v-avatar
          >
        </v-list-item>
        <v-list-item class="mb-2">
          <v-list-item-content>
            <v-list-item-title class="text-h6"> John Doe </v-list-item-title>
            <v-list-item-subtitle>johndoe@gmail.com</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        <v-divider></v-divider>
        <v-list-item-group class="mt-2">
          <v-list-item
            v-for="(item, i) in items"
            :key="i"
            :to="item.text.toLowerCase()"
          >
            <v-list-item-icon>
              <v-icon v-text="item.icon"></v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title v-text="item.text"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group> </v-list
    ></v-navigation-drawer>
  </nav>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";

interface IVListItem {
  readonly text: string;
  readonly icon: string;
}

@Component({})
export default class Navbar extends Vue {
  private drawer = false;
  private items: IVListItem[] = [
    { text: "Chats", icon: "mdi-android-messages" },
    { text: "Contacts", icon: "mdi-account-box" },
    { text: "Archive", icon: "mdi-archive" },
    { text: "Settings", icon: "mdi-cog" },
  ];
}
</script>
<style lang="scss"></style>
