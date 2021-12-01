<template>
  <nav v-if="user">
    <v-app-bar app color="primary pr-2 " absolute flat>
      <v-app-bar-nav-icon
        class="d-md-none"
        dark
        @click="drawer = !drawer"
      ></v-app-bar-nav-icon>
      <v-spacer></v-spacer>
      <v-btn dark icon>
        <v-badge>
          <v-icon>mdi-bell</v-icon>
        </v-badge>
      </v-btn>
      <v-btn dark icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-app-bar>
    <v-navigation-drawer
      v-model="drawer"
      :permanent="$vuetify.breakpoint.mdAndUp"
      app
    >
      <v-list class="mt-2">
        <v-list-item>
          <v-avatar v-if="hasAvatar()" class="mb-2">
            <img :src="user.avatar_url" />
          </v-avatar>
          <v-avatar v-else color="purple" icon class="mb-2">
            <span class="white--text">{{ getInitials() }}</span>
          </v-avatar>
        </v-list-item>
        <v-list-item class="mb-2">
          <v-list-item-content>
            <v-list-item-title class="text-h6">{{
              user.name
            }}</v-list-item-title>
            <v-list-item-subtitle>{{ user.email }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        <v-divider></v-divider>
        <v-list-item-group class="mt-2">
          <v-list-item
            v-for="(item, i) in items"
            :key="i"
            :to="`/${item.text.toLowerCase()}`"
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
import IUser from "../interfaces/user.interface";

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
  get user(): IUser {
    return this.$store.getters["AuthModule/getUser"];
  }

  public hasAvatar(): boolean {
    return !!this.user.avatar_url;
  }

  public getInitials() {
    const splitName = this.user.name.split(" ");
    if (splitName.length <= 1) return splitName[0][0];
    return splitName[0][0] + splitName[1][0];
  }
}
</script>
<style lang="scss"></style>
