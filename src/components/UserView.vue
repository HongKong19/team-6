
<template>
  <div
    v-bind:class="{'user-page-search': (viewingUser == null),
  'user-page-view': (viewingUser != null)
  }"
  >
    <template v-if="viewingUser == null">
      <div class="search-page">
        <div v-if="error != ''" class="alert alert-danger fade show" role="alert">{{ error }}</div>
        <h1>{{searchTitle}}</h1>
        <div class="input-group flex-nowrap" style="margin-top:30px;">
          <div class="input-group-prepend">
            <span class="input-group-text" id="addon-wrapping">@</span>
          </div>
          <input
            type="text"
            class="form-control search-textbox"
            placeholder="Username"
            aria-label="Username"
            aria-describedby="addon-wrapping"
            v-model="query"
          />
        </div>
        <button class="btn btn-main" style="margin-top:30px;" v-on:click="searchUser">
          <font-awesome-icon icon="search" />Search
        </button>
      </div>
    </template>

    <template v-else>
      <div class="col-md-2 profile-sidebar">
        <div class="clear-search" v-on:click="clearUser">
          <font-awesome-icon icon="times" />
        </div>
        <h4>{{viewingUser.username}}</h4>
        <hr>
        <h6 v-if="viewingUser.Email != null">Email: {{viewingUser.Email}}</h6>
        <h6 v-if="viewingUser.Age != null">Age: {{viewingUser.Age}}</h6>
        <h6 v-if="viewingUser.Address != null">Address: {{viewingUser.Address}}</h6>
        <br>
        <h6 v-if="viewingUser.DateRegistered != null">Date Registered: {{viewingUser.DateRegistered}}</h6>

        <hr>

        <button  @click="addToFavorites(viewingUser)" style="margin-top: 15px;" class="btn btn-main">
          <font-awesome-icon icon="user-plus" />Save
        </button>
      </div>
      <div class="col-md-10 profile-main">
        <div class="row">

          <UserDataView/>

        </div>
      </div>
    </template>
  </div>
</template>


<script>
import { mapState } from "vuex";
import UserDataView from "./UserDataView.vue";

export default {
  name: "UserView",
  data() {
    return {
      error: "",
      query: "",
      searchTitle: "Search Customers & Donors"
    };
  },
  methods: {
    searchUser() {
      this.$store.dispatch("searchUser", this.query);
      this.$store.commit('setLoading', true)
    },
    clearUser() {
      this.$store.commit("clearViewingUser");
      this.error = "";
    },
    addToFavorites(user) {
      this.$store.commit("addTeam", user);
    },
    isAdded(id) {
      return (this.favorites.filter(x => x.username == id).length > 0)
    }
  },
  computed: mapState({
    favorites: "favorites",
    menu: "menu",
    viewingUser: "viewingUser"
  }),
  components: {
    UserDataView
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
