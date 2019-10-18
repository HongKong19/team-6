<template>
    <div class="engagement-box">
        <div class="engagement-person">
            <h5>Faisal</h5>
            <button>Email</button>
        </div>
        <hr>
    </div>
</template>

<script>
export default {
    name: "EngagementView",
    data() {
    return {
      title: "Check Likeliness to Donate",
      queryA: "",
      queryB: "",
      error: ""
    };
  }
}
</script>