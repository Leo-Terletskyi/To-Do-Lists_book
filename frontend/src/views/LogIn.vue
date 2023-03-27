<template>
  <div class="log-in">
    <h1 class="h-1">Log in</h1>
    <form class="auth-form" @submit.prevent="submitForm">
      <div class="auth-form__item">
        <h4 class="label">Username:</h4>
        <input type="text" name="username" placeholder="enter your username" v-model="username">
      </div>
      <div class="auth-form__item">
        <h4 class="label">Password:</h4>
        <input type="password" name="password" placeholder="enter you password" v-model="password">
      </div>
      <button class="auth-btn" type="submit">Submit &#10004;</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "LogIn",
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    submitForm() {
      const formData = {
        username: this.username,
        password: this.password
      }
      axios
          .post('/api/v1/auth/token/login/', formData)
          .then(response => {
            console.log(response)
            const token = response.data.auth_token
            console.log(this.$store.state.token)
            this.$store.commit('setToken', token)
            axios.defaults.headers.common['Authorization'] = "Token " + token
            localStorage.setItem("token", token)
            this.$router.push('/to-do-lists')
          })
          .catch(error => {
            console.log(error)
          })
    }
  },
}
</script>

<style scoped>

</style>