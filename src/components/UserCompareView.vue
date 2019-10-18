
<template>
  <div class="container-fluid data-holder" style="background: none">
    <div class="score-card score-card-main">
      <h1>Compatibility Score</h1>
      <radial-progress-bar
        :diameter="200"
        :completed-steps="compatibilityScore"
        :total-steps="100"
        start-color="#4eaba8"
        stop-color="#489290"
        inner-stroke-color="#efefef"
        stroke-width=20
      >
        <h1>{{compatibilityScore}}</h1>
      </radial-progress-bar>
      <hr>
      <center>
      <button
          @click="clearCompare"
          class="btn btn-main"
        >
          New Query
        </button>
        </center>
    </div>
  </div>
</template>


<script>
import { mapState } from "vuex";
import RadialProgressBar from "vue-radial-progress";

export default {
  name: "UserView",
  data() {
    return {
      error: "",
      query: "",
      searchTitle: "Search Github Users"
    };
  },
  methods: {
    clearCompare() {
      this.$store.commit("clearCompareUser");
    }
  },
  computed: mapState({
    compatibilityScore: "compatibilityScore"
  }),
  components: {
    RadialProgressBar
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
