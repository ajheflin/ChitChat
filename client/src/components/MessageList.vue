<template>
  <v-row fluid>
    <v-col>
      <v-list
        two-line
        style="height: 80vh; flex: 1"
        class="mx-auto flex flex-column overflow-auto"
      >
        <template v-for="message in messages">
          <MessageListItem :key="message.id" :user="user" :message="message" />
        </template>
      </v-list>
      <v-form>
        <v-container>
          <v-row>
            <v-col cols="12">
              <v-text-field
                v-model="message"
                append-outer-icon="mdi-send"
                filled
                clear-icon="mdi-close-circle"
                clearable
                label="Message"
                type="text"
              ></v-text-field>
            </v-col>
          </v-row>
        </v-container>
      </v-form>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import IMessage from "../interfaces/message.interface";
import IUser from "../interfaces/user.interface";
import MessageListItem from "./MessageListItem.vue";

@Component({ components: { MessageListItem } })
export default class MessageList extends Vue {
  public message = "";
  private user: IUser = {
    id: "o912u59qawaw5awfn",
    username: "sallyjones",
    name: "SallyJones",
  };
  private messages: IMessage[] = [
    {
      id: "o912u59qawaw5awfn",
      sender: {
        id: "o912u59qawaw5awfn",
        username: "sallyjones",
        name: "Sally Jones",
        profile_photo:
          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQo4p7dS0kGOK3eRnM1W-mJtgc68uRYVGOtRg&usqp=CAU",
      },
      content:
        "Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!",
    },
    {
      id: "o912u59qawaw5awfn",
      sender: {
        id: "o912u59qawaw5awfn",
        username: "sallyjones",
        name: "Sally Jones",
        profile_photo:
          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQo4p7dS0kGOK3eRnM1W-mJtgc68uRYVGOtRg&usqp=CAU",
      },
      content:
        "Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!",
    },
    {
      id: "o912u59qawaw5awfn",
      sender: {
        id: "o912u59qawaw5awfn",
        username: "sallyjones",
        name: "Sally Jones",
        profile_photo:
          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQo4p7dS0kGOK3eRnM1W-mJtgc68uRYVGOtRg&usqp=CAU",
      },
      content:
        "Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!",
    },
    {
      id: "o912u59qawaw5awfn",
      sender: {
        id: "o912u59qawaw5awfn",
        username: "sallyjones",
        name: "Sally Jones",
        profile_photo:
          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQo4p7dS0kGOK3eRnM1W-mJtgc68uRYVGOtRg&usqp=CAU",
      },
      content:
        "Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!",
    },
    {
      id: "o912u59qawaw5awfn",
      sender: {
        id: "o912u59qawaw5awfn",
        username: "sallyjones",
        name: "Sally Jones",
        profile_photo:
          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQo4p7dS0kGOK3eRnM1W-mJtgc68uRYVGOtRg&usqp=CAU",
      },
      content:
        "Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!Hello Jack! Hello Jack!",
    },

    {
      id: "0wja3nga",
      sender: {
        id: "0wja3nga",
        username: "jackjones",
        name: "Jack Jones",
        profile_photo:
          "https://sunrift.com/wp-content/uploads/2014/12/Blake-profile-photo-square.jpg",
      },
      content: "Hello Sally!",
    },
  ];
}
</script>
