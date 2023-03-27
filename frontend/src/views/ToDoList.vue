<template>
 <div class="to-do-list">
    <p>{{ $route.params }}</p>
    <p>{{ this.$route.params.slug }}</p>
    <div v-for="action in toDoList.actions" :key="action.id">
      {{action.title}}
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
            this.toDoList = response.data
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