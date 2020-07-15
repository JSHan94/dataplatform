<template>
  <v-container>
    <v-row justify="start">
      <v-col md="7">
        User: {{user}}
      </v-col>
    </v-row>
    <v-row justify="start">
      <v-col md="7">
        Token: {{balance}}
      </v-col>
    </v-row>
    <v-row justify="start">
      <v-col md="1">
        <v-btn block large color="primary" @click="getToken">
          More Token
        </v-btn>
      </v-col>
    </v-row>
      <v-text-field
        v-model="search"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
      <v-data-table
        :headers="headers"
        :items="datainfo"
        :search="search"
      >
        <template v-slot:item.download = "{item}">
          <v-btn @click="download(item)">download</v-btn>
        </template>
      </v-data-table>
    <v-row justify="center">
      <v-col md="7">
        <v-btn large block @click="analysis">
          analysis
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'
import Web3 from 'web3';
export default {
  data: () => ({
    user: '0x78658C9AaD8523BB283029C43135CF87339ADC21',
    balance: '',
    search: '',
    headers: [
      { text: 'Name', align: 'start', value: 'name', width: "25%"},
      { text: 'Category', align: 'start', value: 'category', width: "10%"},
      { text: 'Price', align: 'start', value: 'price', width: "10%"},
      { text: 'Uploaded Time', align: 'start', value: 'timestamp', width: "20%"},
      { text: 'Download', align: 'center', value: 'download', sortable: false, width: "10%"},
    ],
    datainfo: [
      {
        name: "wrong",
        category: "wrong",
        price: "wrong",
        timestamp: "wrong"
      },
    ]
  }),
  created() {
    axios.get('http://141.223.82.142:3000/userbalance', {
      params: {
        user: this.user
      }
    })
    .then(res => {
      this.balance = res.data
      axios.get('http://141.223.82.142:3000/userdatainfo', {
        params: {
          user: this.user
        }
      })
      .then(res => {
        this.datainfo = res.data.slice()
        this.datainfo.map(temp => {
          temp.timestamp = this.$moment(temp.timestamp).format("YYYY.MM.DD HH:mm:ss")
        })
      })
      .catch(err => {
        console.log(err)
      })
    })
    .catch(err => {
      console.log(err)
    })
  },
  methods:{
    download(item) {
      axios.get('http://141.223.82.142:3000/data', {
        params: {
          datahash: item.datahash
        }
      })
      .then(res => {
        let blob = new Blob([res.data], { type: 'text/plain'})
        let fileName = item.name + ".txt"
        let link = document.createElement('a')
        link.href = window.URL.createObjectURL(blob)
        link.target = '_self'
        link.download = fileName
        link.click()
      })
      .catch(err => {
        console.log(err)
      })
    },
    analysis(){
      window.location.href = "http://localhost:8080"
    },
    getToken(){
      axios.get('http://141.223.82.142:3000/send', {
        params: {
          method: 'getToken',
          user: this.user,
          token: 20
        }
      })
    },
  }
}
</script>