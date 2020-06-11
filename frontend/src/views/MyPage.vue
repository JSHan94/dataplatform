<template>
  <v-col justify="center">
    <v-card>
      <v-card-title>
        <div> {{user}} </div>
        <div> {{balance}} </div>
      </v-card-title>
      <v-card-title>
        <v-text-field
          v-model="search"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="datainfo"
        :search="search"
        @click:row="download"
      >
        <template v-slot:item="row">
          <tr>
            <td>{{row.item.name}}</td>
            <td>{{row.item.category}}</td>
            <td>{{row.item.price}}</td>
            <td>{{row.item.timestamp}}</td>
            <td>
              <v-btn @click="download(row.item)">
              download
              </v-btn>
            </td>
          </tr>
        </template>
      </v-data-table>
    </v-card>
    <v-card>
      <v-col md="1">
        <div class="my-1">
          <v-btn large block @click="analysis">
            analysis
          </v-btn>
        </div>
      </v-col>
    </v-card>
  </v-col>
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
      { text: 'Time', align: 'start', value: 'time', width: "20%"},
      { text: 'Purchase', align: 'start', value: 'time', width: "5%"},
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
      window.location.href = "http://141.223.82.142:8080"
    }
  }
}
</script>