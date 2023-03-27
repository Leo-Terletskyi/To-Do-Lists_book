<template>
  <div class="sign-up">
    <h1 class="h-1">Sign up</h1>
    <form class="auth-form" @submit.prevent="submitForm">
      <div class="auth-form__item">
        <input type="text" name="username" placeholder="enter your username" v-model="username">
      </div>
      <div class="auth-form__item">
        <input type="email" name="email" placeholder="enter your email" v-model="email">
      </div>
      <div class="auth-form__item">
        <input type="password" name="password" placeholder="enter your password" v-model="password">
      </div>
      <button class="auth-btn" type="submit">Sign up</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SignUp",
  data() {
    return {
      username: '',
      email: '',
      password: '',
    }
  },
  methods: {
    submitForm() {
      const formData = {
        username: this.username,
        email: this.email,
        password: this.password,
      }

      axios
          .post('/api/v1/auth/users/', formData)
          .then(response => {
            this.$router.push('/log-in')
            console.log(response)
          })
          .catch(error => {
            console.log(error)
          })
    }
  }
}
</script>

<style scoped>

</style>