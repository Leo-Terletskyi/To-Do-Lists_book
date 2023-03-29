<template>
  <div class="to-do-lists">
    <button type="button" @click="logout">logout</button>
    <h1 class="h-1">&#128221; My to do lists:</h1>
    <div class="to-do-lists__collection">
      <div class="to-do-lists__collection_item">
        <div class="to-do-lists__collection_item-left new-list-col-item-left">
          <div>add new to-do-list:</div>
          <form class="add-new-todolist" @submit.prevent="createNewToDoList">
            <input type="text" name="title" class="new-list-input" maxlength="192" v-model="newToDoList">
            <button type="submit" class="new-list-input-btn">&#9989;</button>
          </form>
        </div>
        <div class="to-do-lists__collection_item-right">
          &#129300;
        </div>
      </div>
      <div class="to-do-lists__collection_item" v-for="list in toDoLists" :key=list.id>
        <div class="to-do-lists__collection_item-left" @click="this.$router.push(`/to-do-lists/${list.slug}`)">
          {{ list.title }}
        </div>
        <div class="to-do-lists__collection_item-right" @click="delToDoList(list)">
          &#10060;
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ToDoLists",
  data() {
    return {
      toDoLists: [],
      newToDoList: ''
    }
  },
  mounted() {
    this.getToDoLists()
  },
  computed: {},
  methods: {
    getToDoLists() {
      axios
          .get('/api/v1/to-do-lists/')
          .then(response => {
            console.log(response.data)
            this.toDoLists = response.data
          })
          .catch(error => {
            console.log(error)
          })
    },
    createNewToDoList() {
      const formData = {
        title: this.newToDoList
      }
      axios
          .post('/api/v1/to-do/create-list/', formData)
          .then(response => {
            console.log(response.data)
            this.toDoLists.unshift(response.data)
            this.newToDoList = ''
          })
          .catch(error => {
            console.log(error)
          })
    },
    delToDoList(toDoList) {
      axios
          .delete(`/api/v1/to-do-lists/${toDoList.slug}`)
          .then(response => {
            this.toDoLists.splice(this.toDoLists.indexOf(toDoList), 1)
          })
          .catch(error => {
            console.log(error)
          })
    },
    logout() {
      this.$store.commit('removeToken')
      this.$router.push('/')
    }
  }
}
</script>

<style scoped>

</style>