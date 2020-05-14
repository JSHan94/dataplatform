<template>
  <v-app>
    <v-content >
      <TopBar></TopBar>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-content>
    <v-footer
      padless
      app
      absolute
    >
      <v-card
        flat
        tile
        class=" grey lighten-2 text-center"
      >
        <v-card-text class=" pt-0">
        </v-card-text>
        <v-divider></v-divider>
      </v-card>
    </v-footer>
  </v-app>
</template>

<script>
import TopBar from './components/TopBar'

export default {
  name: 'App',
  components: {
    TopBar
  },
  data: () => ({
  }),
};
</script>