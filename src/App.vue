<template>
  <div class="body">
    <div class="container-fluid">
      <div class="d-flex row title-bar">
        {{ title }}
      </div>
    </div>

    <div class="container-fluid" style="flex:2;">
      <div class="row" style="height:100%">
        <div class="main-sidebar">
          <div class="main-menu list-group list-group-flush">
            <a
              href="#"
              class="list-group-item list-group-item-action"
              v-bind:class="{'selected': (menu == 'Search')}"
              v-on:click="this.search"
            >
              <font-awesome-icon icon="search" />
            </a>
            <a
              href="#"
              class="list-group-item list-group-item-action"
              v-bind:class="{'selected': (menu == 'Favorites')}"
              v-on:click="this.favorites"
            >
              <font-awesome-icon icon="star" />
            </a>
            <a
              href="#"
              class="list-group-item list-group-item-action"
              v-bind:class="{'selected': (menu == 'Graph')}"
              v-on:click="this.graph"
            >
              <font-awesome-icon icon="project-diagram" />
            </a>
            <a
              href="#"
              class="list-group-item list-group-item-action"
              v-bind:class="{'selected': (menu == 'Compatibility')}"
              v-on:click="this.compatibility"
            >
              <font-awesome-icon icon="balance-scale" />
            </a>

          </div>
        </div>
        <UserView v-if="(menu == 'Search') && (loading != true)" />
        <FavoritesView v-if="(menu == 'Favorites') && (loading != true)" />
        <GraphView v-if="(menu == 'Graph') && (loading != true)"/> 
        <CompatibilityView v-if="(menu == 'Compatibility') && (loading != true)"/>        
        <LoadingView v-if="(loading == true)"/>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import FavoritesView from "./components/FavoritesView.vue";
import UserView from "./components/UserView.vue";
import CompatibilityView from "./components/CompatibilityView.vue";
import LoadingView from "./components/LoadingView.vue";
import GraphView from "./components/GraphView.vue";

export default {
  name: "app",
  data() {
    return {
      title: "Premier Performances Dashboard"
    };
  },
  computed: mapState({
    menu: "menu",
    loading: "loading"
  }),
  methods: {
    search() {
      this.$store.commit("setMenu", "Search");
    },
    favorites() {
      this.$store.commit("setMenu", "Favorites");
    },
    compatibility() {
      this.$store.commit("setMenu", "Compatibility");
    },
    graph() {
      this.$store.commit("setMenu", "Graph");
    }
  },
  components: {
    FavoritesView,
    UserView,
    CompatibilityView,
    LoadingView,
    GraphView
  }
};
</script>

<style>
</style>
