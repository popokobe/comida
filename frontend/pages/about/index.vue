<template>
  <v-layout>
    <h1>This is About Page</h1>
    <v-spacer></v-spacer>
    <div v-for="post in posts" :key="post.id">
      <p>{{ post.name }}</p>
      <p>{{ post.dish }}</p>
      <p>{{ post.created_at }}</p>
      <p>{{ post.note }}</p>
    </div>
  </v-layout>
</template>

<script>
export default {
  data() {
    return {
      posts: []
    }
  },
  async mounted() {
    const url = 'posts'
    const response = await this.$axios.get(url)
    this.posts = response.data
  }
}
</script>
