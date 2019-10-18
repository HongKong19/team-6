
<template>
  <div class="container-fluid data-holder" style="background: none">
    <div class="score-card score-card-main">
      <div class="row">
        <div class="col-md-6">
          <h1>Overall Revenue</h1>
          <radial-progress-bar
            :diameter="200"
            :completed-steps="viewingUser.score"
            :total-steps="100"
            start-color="#4eaba8"
            stop-color="#489290"
            inner-stroke-color="#efefef"
            stroke-width="20"
          >
            <h1>{{viewingUser.score}}</h1>
          </radial-progress-bar>
        </div>

        <div
          class="col-md-6 align-self-center justify-self-center"
          style="border-left: 1px solid #efefef; padding-left: 30px; "
        >
          <div class="row">
            <div class="col-md-9 score-name">
              <h5>Revenue as Donor</h5>
            </div>
            <div class="col-md-3">
              <radial-progress-bar
                :diameter="65"
                :completed-steps="score"
                :total-steps="50000"
                start-color="#4eaba8"
                stop-color="#489290"
                inner-stroke-color="#efefef"
                stroke-width="5"
              >
                <h6>{{viewingUser.RevenueAsDonor}}</h6>
              </radial-progress-bar>
            </div>
          </div>

        <div class="row">
            <div class="col-md-9 score-name">
              <h5>Revenue as Client</h5>
            </div>
            <div class="col-md-3">
              <radial-progress-bar
                :diameter="65"
                :completed-steps="score"
                :total-steps="100000"
                start-color="#4eaba8"
                stop-color="#489290"
                inner-stroke-color="#efefef"
                stroke-width="5"
              >
                <h6>{{viewingUser.RevenueAsClient}}</h6>
              </radial-progress-bar>
            </div>
          </div>
 

        </div>
      </div>
    </div>

    <div class="score-card score-card-main">
      <h3>Concerts Attended</h3>
      <hr />
      <ul v-for="(concert) in viewingUser.ConcertsAttended" v-bind:key="concert">
        <li>{{ concert }}</li>
      </ul>
    </div>

    <!-- <div class="row justify-content-center">
      <div class="score-card">
        <h3>Productivity</h3>
        <hr />
        <div class="java-stat row">
          <div class="col-md-9">Code Additions:</div>
          <div
            class="col-md-3"
            style="color: #86c959;font-weight:bold;text-align:right;"
          >+ {{viewingUser.code_additions}}</div>
        </div>
        <div class="java-stat row">
          <div class="col-md-9">Code Deletions:</div>
          <div
            class="col-md-3"
            style="color: #b0291a; font-weight:bold;text-align:right;"
          >- {{viewingUser.code_deletions}}</div>
        </div>
      </div>

      <div class="score-card">
        <h3>Best Practices</h3>
        <hr />
        <div class="best-practices row">
          <font-awesome-icon v-if="viewingUser.has_maven_gradle" icon="check-square" />
          <font-awesome-icon v-else icon="square" />Uses Maven or Gradle
        </div>
        <div class="best-practices row">
          <font-awesome-icon v-if="viewingUser.has_readme" icon="check-square" />
          <font-awesome-icon v-else icon="square" />Uses Readme
        </div>
        <div class="best-practices row">
          <font-awesome-icon v-if="viewingUser.uses_branches" icon="check-square" />
          <font-awesome-icon v-else icon="square" />Uses Branches
        </div>
      </div>
    </div>
    <div class="row justify-content-center">
      <div class="score-card score-card-third">
        <h3>Code Quality Index</h3>
        <hr />
        <div class="align-self-center justify-self-center">
          <div class="row">
            <radial-progress-bar
              :diameter="200"
              :completed-steps="viewingUser.scores.code_quality"
              :total-steps="100"
              start-color="#4eaba8"
              stop-color="#489290"
              inner-stroke-color="#efefef"
              stroke-width="5"
              style="margin: 0 auto;"
            >
              <h6>{{viewingUser.scores.code_quality}}</h6>
            </radial-progress-bar>
          </div>
        </div>
      </div>

      <div class="score-card score-card-two-thirds">
        <h3>Community Engagement</h3>
        <hr />
        <div class="align-self-center justify-self-center">
          <div class="row">
            <div class="col-md-6 score-name text-center">
              <h6 class="text-center">Comments Quality Score</h6>
            </div>
            <div class="col-md-6 score-name  text-center" >
              <h6 class="text-center">PR Quality Score</h6>
            </div>
            
          </div>
          <div class="row">
            <div class="col-md-6">
              <radial-progress-bar
                :diameter="150"
                :completed-steps="viewingUser.community_scores.comments_quality_score"
                :total-steps="100"
                start-color="#4eaba8"
                stop-color="#489290"
                inner-stroke-color="#efefef"
                stroke-width="5"
                style="margin: 0 auto;"
              >
                <h6>{{viewingUser.community_scores.comments_quality_score}}</h6>
              </radial-progress-bar>
            </div>
            <div class="col-md-6">
              <radial-progress-bar
                :diameter="150"
                :completed-steps="viewingUser.community_scores.pr_quality_score"
                :total-steps="100"
                start-color="#4eaba8"
                stop-color="#489290"
                inner-stroke-color="#efefef"
                stroke-width="5"                
                style="margin: 0 auto;"
              >
                <h6>{{viewingUser.community_scores.pr_quality_score}}</h6>
              </radial-progress-bar>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row align-items-center justify-content-center">
      <div class="score-card">
        <h3>Versatility</h3>
        <hr />
        <div class="row" v-for="dependency in viewingUser.top_dependencies" v-bind:key="dependency">
          <div class="col-md-10 score-name">{{ dependency[0] }}</div>
          <div class="col-md-2">{{ dependency[1] }}</div>
        </div>
      </div>
    </div>
  -->
  </div> 
</template>


<script>
import { mapState } from "vuex";
import RadialProgressBar from "vue-radial-progress";

export default {
  name: "UserView",
  data() {
    return {};
  },
  computed: mapState({
    viewingUser: "viewingUser"
  }),
  components: {
    RadialProgressBar
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
