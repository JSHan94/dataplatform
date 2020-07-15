<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
      clipped
    >
      <v-list flat>
        <v-list-item link @click="$router.push('/').catch(err => {})">
          <v-list-item-action>
            <v-icon>mdi-home</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link @click="$router.push('/Register').catch(err => {})">
          <v-list-item-action>
            <v-icon>mdi-file-upload-outline</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Register</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link @click="$router.push('/Product').catch(err => {})">
          <v-list-item-action>
            <v-icon>mdi-file-search-outline</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Product</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link @click="$router.push('/MyPage').catch(err => {})">
          <v-list-item-action>
            <v-icon>mdi-account-tie</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>MyPage</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <!--
        <v-list-item link @click="$router.push('/Userinfo').catch(err => {})">
          <v-list-item-action>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Userinfo</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link @click="$router.push('/Temp').catch(err => {})">
          <v-list-item-action>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Temp</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        -->
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      clipped-left
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title class="primary--text">Data Exchange Platform</v-toolbar-title>
    </v-app-bar>
    <v-content>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-content>
    <v-footer app>
      <span>&copy; 2020</span>
    </v-footer>
  </v-app>
</template>

<script>

export default {
  name: 'App',
  components: {
  },
  data: () => ({
    drawer: null,
  }),
};
</script>