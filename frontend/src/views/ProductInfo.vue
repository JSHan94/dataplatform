<template>
  <v-container>
    <v-row justify="center">
      <v-col  md="4">
        <v-card outlined>
          <v-card-text>
            <p class="display-1 text--primary"> {{$store.state.productToBuy.name}} </p>
            <div> Category: {{$store.state.productToBuy.category}} </div>
            <div> Price: {{$store.state.productToBuy.price}} </div>
            <div> Uploaded Time: {{$store.state.productToBuy.timestamp}} </div>
            <div> Seller: {{$store.state.productToBuy.owner}} </div>
          </v-card-text>
          <v-card-actions>
            <v-col md="2">
              <v-btn large color="primary" @click="buyProduct($store.state.productToBuy)">
                Buy
              </v-btn>
            </v-col>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Web3 from 'web3';
import axios from 'axios'

export default {
  data: () => ({
  }),
  methods: {
    buyProduct(item) {
      axios.get('http://141.223.82.142:3000/send', {
        params: {
          method: 'buyFile',
          dataHash: item.datahash,
        }
      })
      .then(() => {
      })
      .catch(err => {
        console.log(err)
      })
      alert('거래가 성공적으로 수행되었습니다. 잠시 후 MyPage에서 다운로드가 가능합니다.')
    }
  }
}
</script>