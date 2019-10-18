<template>
  <div class="compare-page">
    <div class="compare-content">
      <h3>{{ loadingMessage }}</h3>
      <div class="spinner-border text-info" role="status">
        <span class="sr-only">Loading...</span>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "CompatibilityView",
  data() {
    return {
      loadingMessage: "Processing Repository Data"
    };
  },

  computed: mapState({
    menu: "menu"
  })
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
