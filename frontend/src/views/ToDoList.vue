<template>
  <div class="to-do-list">
    <h1 class="h-1">&#128212; {{ toDoList.title }}:</h1>
    <h3 class="label">Add new action:</h3>
    <form class="add-action" @submit.prevent="addNewAction">
      <input class="add-action__input" type="text" name="title" v-model="newAction">
      <button type="submit" class="add-action__btn">&#9989;</button>
    </form>
    <div v-for="action in toDoList.actions" :key="action.id" class="to-do-action">
      <div class="to-do-action__title" :class="{ completed: action.completed }" @click="setStatus(action)">{{ action.title }}</div>
      <div class="to-do-action__delete" @click="delToDoAction(action)">
        &#10060;
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ToDoList",
  data() {
    return {
      toDoList: [],
      newAction: ''
    }
  },
  mounted() {
    this.getList()
  },
  methods: {
    getList() {
      axios
          .get(`/api/v1/to-do-lists/${this.$route.params.slug}`)
          .then(response => {
            console.log(response.data)
            this.toDoList = response.data
          })
          .catch(error => {
            console.log(error)
          })
    },
    addNewAction() {
      axios
          .post(`/api/v1/to-do-lists/${this.toDoList.slug}/create-action/`, {title: this.newAction})
          .then(response => {
            this.toDoList.actions.unshift(response.data)
            this.newAction = ''
          })
          .catch(error =>{
            console.log(error)
          })
    },
    setStatus(action) {
      axios
          .put(`/api/v1/to-do-actions/${action.id}/`, {title: action.title, completed: !action.completed})
          .then(response => {
            console.log(response.data)
            const upd_obj = this.toDoList.actions.findIndex((obj => obj.id === action.id));
            this.toDoList.actions[upd_obj].completed = !action.completed
          })
          .catch(error => {
            console.log(error)
          })
    },
    delToDoAction(action) {
      axios
          .delete(`/api/v1/to-do-actions/${action.id}/`)
          .then(response => {
            this.toDoList.actions.splice(this.toDoList.actions.indexOf(action), 1)
          })
          .catch(error => {
            console.log(error)
          })
    },
  }
}
</script>

<style scoped>

</style>