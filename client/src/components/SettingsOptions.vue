<template>
  <v-container>
    <div>
      <h3 class="text-xl text-gray-600">Change Name:</h3>
      <v-text-field
        v-model="newName"
        label="Name"
        hide-details="auto"
      ></v-text-field>
      <v-btn class="mt-5" color="primary" @click="changeName"
        >Change Name</v-btn
      >
    </div>
    <!-- <div>
      <h3 class="text-xl text-gray-500">Change :</h3>
      <v-text-field
        v-model="newName"
        label="Name"
        hide-details="auto"
      ></v-text-field>
    </div> -->
    <!-- v-btn -->
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import axios from "axios";

@Component({})
export default class SettingsOptions extends Vue {
  public newName = "";

  public changeName() {
    // TODO implement axios requests on each change function
    console.log(`Name has been change to ${this.newName}`);
  }
}
</script>
