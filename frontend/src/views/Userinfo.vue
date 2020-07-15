<template>
  <v-col md="8">
    <v-text-field
      v-model="search"
      label="Search"
      single-line
      hide-details
    ></v-text-field>
    <v-data-table
      :headers="headers"
      :items="userinfo"
      :search="search"
    >
    </v-data-table>
  </v-col>
</template>

<script>
import axios from 'axios'
export default {
  data: () => ({
    search: '',
    headers: [
      { text: 'Name', align: 'start', value: 'user', width: "50%"},
      { text: 'Balance', align: 'start', value: 'balance', width: "50%"},
    ],
    userinfo: [
      {
        user: "wrong",
        balance: "wrong",
      },
    ]
  }),
  created() {
    axios.get('http://141.223.82.142:3000/userinfo', {
    })
    .then(res => {
      this.userinfo = res.data.slice()
    })
    .catch(err => {
      console.log(err)
    })
  },
  methods:{
  }
}
</script>