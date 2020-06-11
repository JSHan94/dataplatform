<template>
  <v-row justify = "center">
    <v-col  sm="12" md="8" lg="6" xl="4">
      <v-card>
        <v-card-text>
          <p class="display-1 text--primary"> {{$store.state.productToBuy.name}} </p>
          <div> category: {{$store.state.productToBuy.category}} </div>
          <div> price: {{$store.state.productToBuy.price}} </div>
          <div> time: {{$store.state.productToBuy.timestamp}} </div>
          <p></p>
          <v-text-field v-model="account" label="Account"></v-text-field>
          <v-text-field v-model="passphrase" label="Passphrase"></v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-btn text @click="buyProduct($store.state.productToBuy)">
            Buy
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import Web3 from 'web3';
import axios from 'axios'

export default {
  data: () => ({
    passphrase: 'test0',
    account: '0x95767fDf1Bd84A02DacF1e5cF82fEb49342B7f33',
  }),
  methods: {
    buyProduct(item) {
      axios.get('http://141.223.82.142:3000/send', {
        params: {
          method: 'buyFile',
          dataHash: item.datahash,
        }
      })
      .then(res => {
        alert('거래가 성공적으로 수행되었습니다. 잠시 후 MyPage에서 다운로드가 가능합니다.')
      })
      .catch(err => {
        console.log('error')
      })
    }
  }
}
</script>