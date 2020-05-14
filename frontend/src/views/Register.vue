<template>
  <v-col justify="center">
    <v-text-field v-model="name" label="File Name"></v-text-field>
    <v-text-field v-model="category" label="Category"></v-text-field>
    <v-text-field v-model="price" label="Price"></v-text-field>
    <v-row>
      <input
          type="file"
          @change="onFileChange"
        >
      <v-btn @click="Register">
        Register
      </v-btn>
    </v-row>
  </v-col>
</template>

<script>
import axios from 'axios'
export default {
  data: () => ({
      files: '',
      dData: '',
      name: '',
      category: '',
      price: ''
    }),
  created() {
    /*var web3 = new Web3(new Web3.providers.HttpProvider("http://141.223.85.153:8545"))
    const smartContract = web3.eth.contract(this.abi).at(this.contract)
    if(smartContract.ended())
      this.status="ended"
    else
      this.status="progressing"
    this.fund = smartContract.totalAmount()
    this.owneraccount = smartContract.owner()
    this.owner = web3.fromWei(web3.eth.getBalance(this.owneraccount), 'ether')*/
  },
  methods:{
    /*Register(){
      var web3 = new Web3(new Web3.providers.HttpProvider("http://141.223.85.153:8545"))
      const smartContract = web3.eth.contract(this.abi).at(this.contract)
      web3.personal.unlockAccount(this.account,this.passphrase);
      var transactionObj = { 
        from: this.account,
        to: this.owneraccount,
        value: web3.toWei(0.001, "ether")
      };
      web3.eth.sendTransaction(transactionObj);
    },*/
    onFileChange(e) {
      this.files = e.target.files || e.dataTransfer.files;
    },
    Register () {
      let reader = new FileReader();
        reader.onload = function(e) {
        this.dData = e.target.result
        axios.post('http://localhost:3000/postdata', {
          'data': this.dData
        })
        .then(res => {
          console.log('register-response: ', res)
        })
        .catch(err => {
          console.log('error')
        })
      }
      reader.readAsText(this.files[0])
    }
  }
}
</script>