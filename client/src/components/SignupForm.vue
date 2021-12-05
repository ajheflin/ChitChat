<template>
  <v-container class="px-10">
    <h3 class="text-2xl mt-5 text-center">Signup</h3>
    <v-form
      class="w-full mx-auto md:w-3/4 lg:w-1/4"
      ref="form"
      v-model="valid"
      lazy-validation
    >
      <v-text-field
        v-model="name"
        :rules="nameRules"
        label="Name"
        required
      ></v-text-field>
      <v-text-field
        v-model="email"
        :rules="emailRules"
        label="Email"
        required
      ></v-text-field>
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
      <div class="w-full flex flex-column text-center">
        <v-btn
          :disabled="!valid"
          color="success"
          class="block px-16 md:px-10 md:w-auto mx-auto"
          @click="signup"
        >
          Signup</v-btn
        >
        <p class="mt-3">
          Already have an account? Login
          <router-link to="/login" class="text-blue-500">here</router-link>
        </p>
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
export default class SignupForm extends Vue {
  public valid = true;

  public name = "";
  public nameRules: ValidationRule = [
    (name) => !!name || "Name is required",
    (name) =>
      (name && name.length <= 25) || `Name must be less than 25 characters.`,
  ];

  public username = "";
  public usernameRules: ValidationRule = [
    (username) => !!username || "Username is required",
    (username) =>
      (username && username.length <= 20) ||
      `Username must be less than 20 characters.`,
  ];

  public email = "";
  public emailRules: ValidationRule = [
    (v) => !!v || "E-mail is required",
    (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
  ];

  public password = "";
  public passwordRules: ValidationRule = [
    (password) => !!password || "Password is required",
    (password) =>
      (password && password.length >= 6) ||
      `Password must be at least 6 characters.`,
  ];

  public async signup() {
    if (!(this?.$refs?.form as Vue & { validate: () => boolean }).validate())
      return;
    try {
      const res = await axios.post(`/api/register/`, {
        name: this.name,
        username: this.username,
        password: this.password,
        email: this.email,
      });
      if (res.status === 418)
        throw new Error(
          "Username already exists, please try another username."
        );
      if (res.status === 500)
        throw new Error("Unable to register at this time.");
      this.$store.dispatch("AuthModule/setUser", res.data as IUser);
      this.$router.push(`/${ROUTES.CHATS.toLowerCase()}`);
    } catch (err) {
      console.error(err.message);
    }
  }
}
</script>
