<template>
  <v-container>
    <div>
      <h3 class="text-xl text-gray-600">Change Name:</h3>
      <v-text-field
        v-model="newName"
        label="Name"
        hide-details="auto"
      ></v-text-field>
      <v-btn class="mt-5" color="primary" @click="changeName">
        Change Name
      </v-btn>
    </div>

    <div>
      <h3 class="text-xl text-gray-500">Change Username:</h3>
      <v-text-field
        v-model="newUsername"
        label="Username"
        hide-details="auto"
      ></v-text-field>
    </div>
    <v-btn class="mt-5" color="primary" @click="changeUN">
      Change Username
    </v-btn>

    <div>
      <h3 class="text-xl text-gray-500">Change Password:</h3>
      <v-text-field
        v-model="currentPassword"
        label="Current Password"
        hide-details="auto"
      ></v-text-field>
      <v-text-field
        v-model="newPassword"
        label="New Password"
        hide-details="auto"
      ></v-text-field>
      <v-text-field
        v-model="confirmNew"
        label="Confirm New Password"
        hide-details="auto"
      ></v-text-field>
    </div>
    <v-btn class="mt-5" color="primary" @click="changePass">
      Change Password
    </v-btn>

    <div>
      <h3 class="text-xl text-gray-500">Delete Account</h3>
    </div>

    <div>
      <v-dialog v-model="dialog" width="500">
        <template v-slot:activator="{ on, attrs }">
          <v-btn color="red" dark v-bind="attrs" v-on="on"> Delete </v-btn>
        </template>

        <v-card>
          <v-card-title class="text-h5 grey lighten-2">
            Delete Account?
          </v-card-title>

          <v-card-text>
            Are you sure you want to delete your account?
          </v-card-text>

          <v-divider></v-divider>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" text @click="deleteAccount">
              Yes, I'm Sure
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </div>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import axios from "axios";

@Component({})
export default class SettingsOptions extends Vue {
  public newName = "";
  public newUsername = "";
  public newPassword = "";
  public confirmNew = "";
  public currentPassword = "";
  public dialog = false;

  get user() {
    return this.$store.getters["AuthModule/getUser"];
  }

  public async changeName() {
    await axios.post("/api/users/changeName/", {
      user_id: this.user.id,
      newName: this.newName,
    });
  }

  public async changeUN() {
    await axios.post("/api/users/changeUsername/", {
      user_id: this.user.id,
      newUsername: this.newUsername,
    });
  }

  public async changePass() {
    if (this.newPassword == this.confirmNew) {
      await axios.post("/api/users/changePass/", {
        user_id: this.user.id,
        newPassword: this.newPassword,
      });
    }
  }

  public async deleteAccount() {
    await axios.get(`/api/users/delete/${this.user.id}`);
    this.dialog = false;
  }
}
</script>
