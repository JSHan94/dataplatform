<template>
  <v-col>
    <v-tabs :centered="true" v-model="tab">
      <v-tab v-for="item in data" :key="item.tab">
        {{item.tab}}
      </v-tab>
    </v-tabs>
    <v-tabs-items v-model="tab">
      <v-tab-item v-for="item in data" :key="item.tab">
        <v-col>
          <v-text-field
            v-model="search"
            label="Search"
            single-line
            hide-details
          ></v-text-field>
          <v-data-table
            :headers="headers"
            :items="item.table"
            :search="search"
          >
            <template v-slot:item.buy = "{item}">
              <v-btn color="primary" @click="buy(item)">buy</v-btn>
            </template>
          </v-data-table>
        </v-col>
      </v-tab-item>
    </v-tabs-items>
  </v-col>
</template>

<script>
import axios from "axios"

export default {
    data: () => ({
      tab: null,
      search: '',
      headers: [
        { text: 'Name', align: 'start', value: 'name', width: "25%"},
        { text: 'Category', align: 'start', value: 'category', width: "10%"},
        { text: 'Price', align: 'start', value: 'price', width: "10%"},
        { text: 'Uploaded Time', align: 'start', value: 'timestamp', width: "20%"},
        { text: 'Purchase', align: 'center', value: 'buy', sortable: false, width: "5%"},
      ],
      datainfo: [
        {
          name: "wrong",
          category: "Blockchain",
          price: "wrong",
          timestamp: "wrong"
        },
      ],
      data: [
        {tab: 'Blockchain', table: []},
        {tab: 'Health', table: []},
        {tab: 'Money', table: []},
        {tab: 'Device', table: []},
        {tab: 'Weather', table: []},
      ]
    }),
    created() {
      axios.get('http://141.223.82.142:3000/datainfo', {params: {'start': 0, 'end': 20}})
      .then(res => {
        this.datainfo = res.data.slice()
        this.datainfo.map(temp => {
          if(temp.category=='Blockchain')
            this.data[0].table.push(temp)
          else if(temp.category=='Health')
            this.data[1].table.push(temp)
          else if(temp.category=='Money')
            this.data[2].table.push(temp)
          else if(temp.category=='Device')
            this.data[3].table.push(temp)
          else if(temp.category=='Weather')
            this.data[4].table.push(temp)
        })
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
      },
      see() {
        console.log(this.data[0].table)
      }
    }
}
</script>