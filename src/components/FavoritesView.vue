<template>
  <div class="container page-content">
    <h2>{{title}}</h2>
    <hr />
    <div class="list-group list-group-flush">
      <div class="fav-user row" v-for="user in favorites" :key="user.id">
        <div class="col-md-3">
          <div class="pfp">
            <img :src="user.avatar" />
          </div>
        </div>
        <div class="col-md-6">
          <h4>{{user.username}}</h4>
          <h4 class="subtitle">Developer Score: {{user.overall_score}}</h4>
          <hr />
          <h6>{{user.name}}</h6>
          <h6>{{user.company}}</h6>
          <h6>{{user.location}}</h6>
        </div>
        <div class="col-md-3">
          <button style="margin-right: 10px" class="btn btn-main" v-on:click="viewUser(user)">
            <font-awesome-icon icon="newspaper" /> Report
          </button>
          <button class="btn btn-delete" v-on:click="del(user.username)">
            <font-awesome-icon icon="times" />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "FavoritesView",
  data() {
    return {
      title: "Top Donors"
    };
  },
  methods: {
    del(id) {
      this.$store.commit("deleteTeam", id);
    },
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
