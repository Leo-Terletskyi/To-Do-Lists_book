<template>
  <div class="auth">
    <div class="auth__sign-up">
      <router-link to="/sign-up">Sign up &#128196;</router-link>
    </div>
    <div class="auth__login">
      <router-link to="/log-in">Log in &#128195;</router-link>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Auth",
  data() {
    return {

    }
  },
  beforeCreate() {
    if (this.$store.state.token) {
      this.$router.push('/to-do-lists')
    }
  },
  methods: {
  }
}
</script>

<style scoped>

</style>