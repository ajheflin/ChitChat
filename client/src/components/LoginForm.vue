<template>
  <v-container class="px-10">
    <h3 class="text-2xl mt-5 text-center">Login</h3>
    <v-form
      class="w-full mx-auto md:w-3/4 lg:w-1/4"
      ref="form"
      v-model="valid"
      lazy-validation
    >
      <v-text-field
        v-model="username"
        :rules="usernameRules"
        label="Username"
        required
      ></v-text-field>

      <v-text-field
        type="password"
        v-model="password"
        :rules="passwordRules"
        label="Password"
        required
      ></v-text-field>
      <div class="w-full">
        <v-btn
          :disabled="!valid"
          color="success"
          class="block px-16 md:px-10 md:w-auto mx-auto"
          @click="login"
        >
          Login</v-btn
        >
      </div>
    </v-form>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import axios from "axios";
import IUser from "../interfaces/user.interface";
import { ROUTES } from "../router/routes";
import { ValidationRule } from "../types/validation-rules.type";
@Component({})
export default class LoginForm extends Vue {
  public valid = true;

  public username = "";
  public usernameRules: ValidationRule = [
    (username) => !!username || "Username is required",
    (username) =>
      (username && username.length <= 20) ||
      `Username must be less than 20 characters.`,
  ];
  public password = "";
  public passwordRules: ValidationRule = [
    (password) => !!password || "Password is required",
    (password) =>
      (password && password.length >= 6) ||
      `Password must be at least 6 characters.`,
  ];

  public async login() {
    if (!(this?.$refs?.form as Vue & { validate: () => boolean }).validate())
      return;
    try {
      const res = await axios.post(`api/auth/`, {
        username: this.username,
        password: this.password,
      });
      if (res.status === 401)
        throw new Error("Invalid username and password combination");
      this.$store.dispatch("AuthModule/setUser", res.data as IUser);
      this.$router.push(`/${ROUTES.CHATS.toLowerCase()}`);
    } catch (err) {
      console.error(err.message);
    }
  }
}
</script>
