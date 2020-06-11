<template>
  <v-card>
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
      @click:row="buy"
    >
      <template v-slot:item="row">
        <tr>
          <td>{{row.item.name}}</td>
          <td>{{row.item.category}}</td>
          <td>{{row.item.price}}</td>
          <td>{{row.item.timestamp}}</td>
          <td>
            <v-btn @click="buy(row.item)">
            buy
            </v-btn>
          </td>
        </tr>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
import axios from "axios"

export default {
    data: () => ({
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
      axios.get('http://141.223.82.142:3000/datainfo')
      .then(res => {
        this.datainfo = res.data.slice()
      })
      .catch(err => {
        console.log(err)
      })
    },
    methods: {
      buy(item) {
        let number = item.price
        this.$store.state.productToBuy = item
        let a = number.toString()  
        this.$router.push({name: 'ProductInfo', params: {id: a}})
      }
    }
}
</script>