<template>
    <h1>{{ title }}</h1>
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