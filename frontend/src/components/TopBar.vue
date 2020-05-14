<template>
    <v-toolbar>
        <v-toolbar-title>Data Exchange Platform</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items>
            <v-btn
                v-for="(link, i) in $store.state.Links"
                :key = "i"
                :to = "{name: link.routerName}"
                exact
                text
            >
                {{link.name}}
            </v-btn>
        </v-toolbar-items>
    </v-toolbar>

</template>

<script>
export default {
    data () {
      return {
        model: 'tab-2',
      }
    },
    computed:{
    }
    
}
</script>