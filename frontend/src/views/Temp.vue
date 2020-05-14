<template>
  <v-col justify="center">
    <v-row>
      <v-btn
        :to = "{name: 'Home'}">
        {{"go to main"}}
      </v-btn>
    </v-row>
    <v-row>
      <p>status: {{status}}</p>
    </v-row>
    <v-row>
      <p>The amount of currently funded ETH: {{fund}}</p>
    </v-row>
    <v-row>
      <p>The amount of ETH which owner holds: {{owner}}</p>
    </v-row>
    <v-text-field v-model="account" label="Account to fund"></v-text-field>
    <v-text-field v-model="amount" label="The amount of funding"></v-text-field>
    <v-text-field v-model="passphrase" label="Passphrase"></v-text-field>
    <v-row>
      <v-btn @click="funding">
        funding
      </v-btn>
    </v-row>
  </v-col>
</template>

<script>

export default {
  data() {
    return {
      status: '',
      fund: '',
      owner: '',
      account: '',
      amount: '',
      passphrase: '',
      owneraccount: '',
      contract: '0x2105Ee1267F647DA00b5c56171fD7C438Baa3a09',
      abi: [{"constant": false,"inputs": [],"name": "checkGoalReached","outputs": [],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": true,"inputs": [],"name": "ended","outputs": [{"name": "","type": "bool"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": true,"inputs": [],"name": "totalAmount","outputs": [{"name": "","type": "uint256"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": true,"inputs": [],"name": "goalAmount","outputs": [{"name": "","type": "uint256"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": true,"inputs": [],"name": "deadline","outputs": [{"name": "","type": "uint256"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": false,"inputs": [],"name": "withdraw","outputs": [],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": false,"inputs": [],"name": "kill","outputs": [],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": true,"inputs": [],"name": "tokenReward","outputs": [{"name": "","type": "address"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": true,"inputs": [{"name": "","type": "address"}],"name": "balanceOf","outputs": [{"name": "","type": "uint256"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": true,"inputs": [],"name": "goalReached","outputs": [{"name": "","type": "bool"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": true,"inputs": [],"name": "owner","outputs": [{"name": "","type": "address"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": true,"inputs": [],"name": "price","outputs": [{"name": "","type": "uint256"}],"payable": false,"stateMutability": "view","type": "function"},{"constant": false,"inputs": [{"name": "_excess","type": "uint256"}],"name": "withdrawExcess","outputs": [],"payable": false,"stateMutability": "nonpayable","type": "function"},{"inputs": [{"name": "_goalAmount","type": "uint256"},{"name": "_durationMinutes","type": "uint256"},{"name": "_costOfToken","type": "uint256"},{"name": "_tokenAddress","type": "address"}],"payable": false,"stateMutability": "nonpayable","type": "constructor"},{"payable": true,"stateMutability": "payable","type": "fallback"},{"anonymous": false,"inputs": [{"indexed": false,"name": "ownerAddress","type": "address"},{"indexed": false,"name": "amountRaisedValue","type": "uint256"}],"name": "GoalReached","type": "event"},{"anonymous": false,"inputs": [{"indexed": false,"name": "backer","type": "address"},{"indexed": false,"name": "amount","type": "uint256"},{"indexed": false,"name": "isContribution","type": "bool"}],"name": "FundTransfer","type": "event"}],
    }
  },
  created() {
    var web3 = new Web3(new Web3.providers.HttpProvider("http://141.223.85.153:8545"))
    const smartContract = web3.eth.contract(this.abi).at(this.contract)
    if(smartContract.ended())
      this.status="ended"
    else
      this.status="progressing"
    this.fund = smartContract.totalAmount()
    this.owneraccount = smartContract.owner()
    this.owner = web3.fromWei(web3.eth.getBalance(this.owneraccount), 'ether')
  },
  methods:{
    funding(){
      var web3 = new Web3(new Web3.providers.HttpProvider("http://141.223.85.153:8545"))
      const smartContract = web3.eth.contract(this.abi).at(this.contract)
      web3.personal.unlockAccount(this.account,this.passphrase);
      var transactionObj = { 
        from: this.account,
        to: this.owneraccount,
        value: web3.toWei(0.001, "ether")
      };
      web3.eth.sendTransaction(transactionObj);
    },
  }
}
</script>