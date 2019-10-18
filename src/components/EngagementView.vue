<template>
  <div class="container page-content">
    <h2>{{title}}</h2>
    <hr />
    <div class="list-group list-group-flush">
      <div class="fav-user row boxing" v-for="user in favorites" :key="user.id">
        <div>
          <h4>{{user.username}}</h4>
          <h4 class="subtitle">Total Donation Made: {{user.overall_score}}</h4>
          <hr />
        </div>
        <div>
          <button class="btn btn-main box-img" v-on:click="viewUser(user)">
            <font-awesome-icon icon="newspaper" /> Email
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "EngagementView",
  data() {
    return {
      title: "Engagement"
    };
  },
  methods: {
    viewUser(user) {
      this.$store.commit("setViewingUser", user);
      this.$store.commit("setMenu", "Search");
    }
  },
  computed: mapState({
    favorites: "favorites",
    menu: "menu"
  })
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
