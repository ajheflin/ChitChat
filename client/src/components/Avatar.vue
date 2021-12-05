<template>
  <v-avatar
    v-if="image"
    color="indigo"
    :size="$vuetify.breakpoint.mdAndUp ? 65 : 55"
    class="white--text mr-5"
  >
    <v-img :src="image" />
    <!-- <span
      :class="$vuetify.breakpoint.mdAndUp ? 'text-h6 font-weight-regular' : ''"
      v-else
      >{{ getNameAbbrev(user.name) }}</span
    > -->
  </v-avatar>
</template>

<script lang="ts">
import Vue from "vue";
import Component from "vue-class-component";
import { Prop } from "vue-property-decorator";
// import IUser from "../interfaces/user.interface";

@Component({})
export default class Avatar extends Vue {
  // @Prop({}) user: IUser | undefined;
  @Prop() image: string | undefined;
  // getNameAbbrev(name: string) {
  //   const [first, last] = name.split(" ");
  //   return `${first[0]}${last[0]}`;
  // }
}
</script>
