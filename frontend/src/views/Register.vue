<template>
  <v-col justify="center">
    <v-text-field v-model="name" label="File Name"></v-text-field>
    <v-text-field v-model="category" label="Category"></v-text-field>
    <v-text-field v-model="price" label="Price"></v-text-field>
    <!--  이더리움 연결 테스트 용
    <v-row>
      <p>owner: {{owner}}</p>
    </v-row>
    <v-row>
      <p>ETH: {{eth}}</p>
    </v-row>
    -->
    <v-row>
      <input
          type="file"
          @change="onFileChange"
        >
      <v-btn @click="upload">
        upload
      </v-btn>
    </v-row>
    <v-row>
      <v-btn @click="register">
        register
      </v-btn>
    </v-row>
    <!--
    <v-row>
      <v-btn @click="see">
        see
      </v-btn>
    </v-row>
    -->
  </v-col>
</template>

<script>
import axios from 'axios'
import Web3 from 'web3';

export default {
  data: () => ({
      files: '',
      dData: '',
      name: '',
      category: '',
      price: '',
      eth: '',
      owner: '0x95767fDf1Bd84A02DacF1e5cF82fEb49342B7f33',
      passphrase: 'test0',
      datah: '1',
      account: '0x95767fDf1Bd84A02DacF1e5cF82fEb49342B7f33',
      abi: [
            {
              "anonymous": false,
              "inputs": [
                {
                  "indexed": false,
                  "internalType": "address",
                  "name": "_from",
                  "type": "address"
                },
                {
                  "indexed": false,
                  "internalType": "uint256",
                  "name": "_balance",
                  "type": "uint256"
                }
              ],
              "name": "Balance",
              "type": "event"
            },
            {
              "inputs": [
                {
                  "internalType": "uint256",
                  "name": "_datah",
                  "type": "uint256"
                }
              ],
              "name": "buy",
              "outputs": [],
              "stateMutability": "payable",
              "type": "function"
            },
            {
              "anonymous": false,
              "inputs": [
                {
                  "indexed": false,
                  "internalType": "address",
                  "name": "_from",
                  "type": "address"
                },
                {
                  "indexed": false,
                  "internalType": "address",
                  "name": "_to",
                  "type": "address"
                },
                {
                  "indexed": false,
                  "internalType": "uint256",
                  "name": "_datah",
                  "type": "uint256"
                }
              ],
              "name": "Buy",
              "type": "event"
            },
            {
              "inputs": [
                {
                  "internalType": "uint256",
                  "name": "_datah",
                  "type": "uint256"
                }
              ],
              "name": "getData",
              "outputs": [],
              "stateMutability": "nonpayable",
              "type": "function"
            },
            {
              "anonymous": false,
              "inputs": [
                {
                  "indexed": false,
                  "internalType": "uint256",
                  "name": "timestamp",
                  "type": "uint256"
                },
                {
                  "indexed": false,
                  "internalType": "string",
                  "name": "category",
                  "type": "string"
                },
                {
                  "indexed": false,
                  "internalType": "string",
                  "name": "name",
                  "type": "string"
                },
                {
                  "indexed": false,
                  "internalType": "uint256",
                  "name": "datah",
                  "type": "uint256"
                },
                {
                  "indexed": false,
                  "internalType": "uint256",
                  "name": "price",
                  "type": "uint256"
                },
                {
                  "indexed": false,
                  "internalType": "enum TradingPlatform.STATE",
                  "name": "state",
                  "type": "uint8"
                },
                {
                  "indexed": false,
                  "internalType": "address",
                  "name": "owner",
                  "type": "address"
                },
                {
                  "indexed": false,
                  "internalType": "address",
                  "name": "buyer",
                  "type": "address"
                }
              ],
              "name": "GetData",
              "type": "event"
            },
            {
              "inputs": [
                {
                  "internalType": "uint256",
                  "name": "_token",
                  "type": "uint256"
                }
              ],
              "name": "giveToken",
              "outputs": [],
              "stateMutability": "nonpayable",
              "type": "function"
            },
            {
              "inputs": [
                {
                  "internalType": "uint256",
                  "name": "_datah",
                  "type": "uint256"
                }
              ],
              "name": "salesConfirm",
              "outputs": [],
              "stateMutability": "nonpayable",
              "type": "function"
            },
            {
              "inputs": [
                {
                  "internalType": "string",
                  "name": "_category",
                  "type": "string"
                },
                {
                  "internalType": "string",
                  "name": "_name",
                  "type": "string"
                },
                {
                  "internalType": "uint256",
                  "name": "_datah",
                  "type": "uint256"
                },
                {
                  "internalType": "uint256",
                  "name": "_price",
                  "type": "uint256"
                }
              ],
              "name": "upload",
              "outputs": [],
              "stateMutability": "nonpayable",
              "type": "function"
            },
            {
              "anonymous": false,
              "inputs": [
                {
                  "indexed": false,
                  "internalType": "string",
                  "name": "_category",
                  "type": "string"
                },
                {
                  "indexed": false,
                  "internalType": "string",
                  "name": "_name",
                  "type": "string"
                },
                {
                  "indexed": false,
                  "internalType": "uint256",
                  "name": "_datah",
                  "type": "uint256"
                },
                {
                  "indexed": false,
                  "internalType": "uint256",
                  "name": "_price",
                  "type": "uint256"
                }
              ],
              "name": "Upload",
              "type": "event"
            },
            {
              "inputs": [
                {
                  "internalType": "address",
                  "name": "",
                  "type": "address"
                }
              ],
              "name": "balanceOf",
              "outputs": [
                {
                  "internalType": "uint256",
                  "name": "",
                  "type": "uint256"
                }
              ],
              "stateMutability": "view",
              "type": "function"
            }
          ],
        contract: '0x6a4D4361989E8e092541F96891F8d559a3E86700',
    }),
  async created() {  //이더리움 연결 테스트 용
    /*
    var web3 = new Web3(new Web3.providers.HttpProvider("http://141.223.82.138:8080"))
    this.eth = await web3.eth.getBalance(this.owner);
    */
  },
  methods:{
    register(){ //smart contract 테스트 중
      /* 
      var web3 = new Web3(new Web3.providers.HttpProvider("http://141.223.82.138:8080"))
      const smartContract = new web3.eth.Contract(this.abi,this.contract)
      web3.eth.personal.unlockAccount(this.account,this.passphrase);
      smartContract.methods.upload(this.category, this.name, this.datah, this.price).call({ from: this.account, gas: 1000000 }).then(console.log('ok'));
      */
    },
    see(){ //smart contract 테스트 중
      /*
      var web3 = new Web3(new Web3.providers.HttpProvider("http://141.223.82.138:8080"))
      const smartContract = new web3.eth.Contract(this.abi,this.contract)
      web3.eth.personal.unlockAccount(this.account,this.passphrase);
      smartContract.methods.getData(100).call({from: this.account, gas: 1000000 }).then(
        smartContract.events.GetData((err,event) => {console.log(event)})
      )
      /*smartContract.getPastEvents('GetData', {
    fromBlock: 0,
    toBlock: 'latest'
}, function(error, events){ console.log(events); })*/
    },
    onFileChange(e) {
      this.files = e.target.files || e.dataTransfer.files;
    },
    upload () {
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