<template>
  <nav>
    <v-toolbar>
      <v-toolbar-title>
        <v-btn to="/home" nuxt>Comida</v-btn>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn v-if="!loggedIn" to="/login" nuxt dark class="mx-1"
        >ログイン</v-btn
      >
      <v-btn v-if="!loggedIn" to="/register" nuxt dark class="mx-1">登録</v-btn>
      <v-btn v-if="loggedIn" @click="logout" dark class="mx-1"
        >ログアウト</v-btn
      >
    </v-toolbar>
  </nav>
</template>

<script>
export default {
  data() {
    return {}
  },
  computed: {
    loggedIn() {
      return this.$store.getters.loggedIn
    }
  },
  methods: {
    logout() {
      this.$store.dispatch('logout')
    }
  }
}
</script>
