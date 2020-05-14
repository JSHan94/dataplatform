<template>
  <v-row justify="center">
    <v-col cols = "12">
      <v-tabs center-active fixed-tabs>
        <v-tab v-for="item in datainfo" :key="item">{{item.category}}</v-tab>
      </v-tabs>
    </v-col>
    <v-col v-for="item in datainfo" :key="item.iddatainfo" cols="auto">
      <v-card max-width="400px">
        <v-card-text>
          <p class="display-1 text--primary"> {{item.name}} </p>
          <div> price: {{item.price}} </div>
          <p> time: {{item.time}} </p>
        </v-card-text>
        <v-card-actions>
          <v-btn text>Buy</v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import axios from "axios"

export default {
    data: () => ({
        datainfo: []
    }),
    created() {
        axios.get('http://localhost:3000/datainfo', {params: {'start': 0, 'end': 20}})
        .then(res => {
            this.datainfo = res.data.slice()
        })
        .catch( err => {
            console.log('error to loading datainfo')
        })
    },
    methods: {
    }
}
</script>