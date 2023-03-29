<template>
  <div class="not-found">
    <h1 class="h-1"><span class="emoji">&#128533;</span> We lost this page</h1>
    <p class="h-1">We searched high and low but couldn't find what you're looking for.</p>
    <p class="h-1">Let's find a better place for you to go.</p>
    <button class="to-home-page-btn" type="button" @click="this.$router.push('/')">Home page</button>
  </div>
</template>

<script>
export default {
  name: "Http404"
}
</script>

<style scoped>

</style>