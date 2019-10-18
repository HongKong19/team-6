
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
        <img :src="viewingUser.avatar" />
        <h4>{{viewingUser.username}}</h4>
        <hr>
        <h6 v-if="viewingUser.name != null">{{viewingUser.name}}</h6>
        <h6 v-if="viewingUser.company != null">{{viewingUser.company}}</h6>
        <h6 v-if="viewingUser.location != null">{{viewingUser.location}}</h6>
        <p v-if="viewingUser.bio != null" style="padding: 20px 0;">{{viewingUser.bio}}</p>
        <hr>
        <button class="btn btn-sec" v-if="viewingUser.email != null">
          <font-awesome-icon icon="envelope" />Contact
        </button>
        <button v-if="isAdded(viewingUser.username)" style="margin-top: 15px;" class="btn btn-main" disabled>
          <font-awesome-icon icon="user-check" />Saved
        </button> 
        <button v-else @click="addToFavorites(viewingUser)" style="margin-top: 15px;" class="btn btn-main">
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
