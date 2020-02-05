<template>
  <v-app>
    <Navigation />
    <v-content>
      <v-container>
        <nuxt />
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import Navigation from '~/components/Navigation'
export default {
  components: {
    Navigation
  },
  data() {
    return {}
  }
}
</script>
