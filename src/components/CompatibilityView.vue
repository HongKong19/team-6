<template>
  <div class="compare-page">
    <template v-if="compareUser == null">
      <div class="compare-content">
        <h1>{{title}}</h1>
        <div class="input-group flex-nowrap" style="margin-top:30px;">
          <div class="input-group-prepend">
            <span class="input-group-text" id="addon-wrapping">@</span>
          </div>
          <input
            type="text"
            class="form-control search-textbox"
            placeholder="Username"
            v-model="queryA"
          />
          <div class="input-group-append">
            <b-button
              v-b-modal.chooseSavedA
              class="btn btn-sec-small"
              type="button"
              id="button-addon1"
            >
              <font-awesome-icon icon="star" />Saved Users
            </b-button>
          </div>
        </div>
        <div class="compare-icon">
          <font-awesome-icon icon="exchange-alt" />
        </div>
        <div class="input-group flex-nowrap">
          <div class="input-group-prepend">
            <span class="input-group-text" id="addon-wrapping">@</span>
          </div>
          <input
            type="text"
            class="form-control search-textbox"
            placeholder="Username"
            v-model="queryB"
          />
          <div class="input-group-append">
            <b-button
              v-b-modal.chooseSavedB
              class="btn btn-sec-small"
              type="button"
              id="button-addon2"
            >
              <font-awesome-icon icon="star" />Saved Users
            </b-button>
          </div>
        </div>
        <button class="btn btn-main" @click="compare" style="margin-top:30px;">
          <font-awesome-icon icon="balance-scale" />Compare
        </button>
      </div>
    </template>

    <template v-else>
      <div class="col-md-2 profile-sidebar" style="padding-top: 30px;">
        <img :src="compareUser[0].avatar" />
        <h4>{{compareUser[0].Name}}</h4>
        <hr />
        <h6 v-if="compareUser[0].name != null">{{compareUser[0].name}}</h6>
        <h6 v-if="compareUser[0].company != null">{{compareUser[0].company}}</h6>
        <h6 v-if="compareUser[0].location != null">{{compareUser[0].location}}</h6>
        <p v-if="compareUser[0].bio != null" style="padding: 20px 0;">{{compareUser[0].bio}}</p>
        <hr />
        <button class="btn btn-sec" v-if="compareUser[0].email != null">
          <font-awesome-icon icon="envelope" />Contact
        </button>
        <button
          v-if="isAdded(compareUser[0].username)"
          style="margin-top: 15px;"
          class="btn btn-main"
          disabled
        >
          <font-awesome-icon icon="user-check" />Saved
        </button>
        <button
          v-else
          @click="addToFavorites(compareUser[0])"
          style="margin-top: 15px;"
          class="btn btn-main"
        >
          <font-awesome-icon icon="user-plus" />Save
        </button>
      </div>
      <div class="col-md-8 comparison-main">
        <div class="row">
          <UserCompareView />
        </div>
      </div>
      <div class="col-md-2 profile-sidebar" style="padding-top: 30px;">
        <img :src="compareUser[1].avatar" />
        <h4>{{compareUser[1].Name}}</h4>
        <hr />
        <h6 v-if="compareUser[1].name != null">{{compareUser[1].name}}</h6>
        <h6 v-if="compareUser[1].company != null">{{compareUser[1].company}}</h6>
        <h6 v-if="compareUser[1].location != null">{{compareUser[1].location}}</h6>
        <p v-if="compareUser[1].bio != null" style="padding: 20px 0;">{{compareUser[1].bio}}</p>
        <hr />
        <button class="btn btn-sec" v-if="compareUser[1].email != null">
          <font-awesome-icon icon="envelope" />Contact
        </button>
        <button
          v-if="isAdded(compareUser[1].username)"
          style="margin-top: 15px;"
          class="btn btn-main"
          disabled
        >
          <font-awesome-icon icon="user-check" />Saved
        </button>
        <button
          v-else
          @click="addToFavorites(compareUser[1])"
          style="margin-top: 15px;"
          class="btn btn-main"
        >
          <font-awesome-icon icon="user-plus" />Save
        </button>
      </div>
    </template>

    <b-modal ref="cs" id="chooseSavedA" title="Saved Users" hide-footer>
      <form>
        <div class="form-group">
          <label for="name">Select a user from your saved users.</label>
          <div class="list-group list-group-flush">
            <a
              v-for="user in favorites"
              v-bind:key="user.username"
              @click="chooseSaved('chooseSavedA', user.username)"
              href="#"
              class="list-group-item list-group-item-action"
            >{{user.username}}</a>
          </div>
        </div>
      </form>
    </b-modal>

    <b-modal ref="cs" id="chooseSavedB" title="Saved Users" hide-footer>
      <form>
        <div class="form-group">
          <label for="name">Select a user from your saved users.</label>
          <div class="list-group list-group-flush">
            <a
              v-for="user in favorites"
              v-bind:key="user.username"
              @click="chooseSaved('chooseSavedB', user.username)"
              href="#"
              class="list-group-item list-group-item-action"
            >{{user.username}}</a>
          </div>
        </div>
      </form>
    </b-modal>
  </div>
</template>

<script>
import { mapState } from "vuex";
import UserCompareView from "./UserCompareView.vue";

export default {
  name: "CompatibilityView",
  data() {
    return {
      title: "Check Likeliness to Donate",
      queryA: "",
      queryB: "",
      error: ""
    };
  },
  methods: {
    compare() {
      console.log(this.queryA, this.queryB)
      this.$store.commit('setLoading', true)
      this.$store.dispatch("compareUsers", [this.queryA, this.queryB]);
    },
    chooseSaved(modal, id) {
      if (modal == "chooseSavedB") {
        this.queryB = id;
        this.$refs["cs"].hide("chooseSavedB");
      } else {
        this.queryA = id;
        this.$refs["cs"].hide("chooseSavedA");
      }
    },
    addToFavorites(user) {
      this.$store.commit("addTeam", user);
    },
    isAdded(id) {
      return this.favorites.filter(x => x.username == id).length > 0;
    }
  },

  computed: mapState({
    favorites: "favorites",
    menu: "menu",
    compareUser: "compareUser"
  }),
  components: {
    UserCompareView
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
