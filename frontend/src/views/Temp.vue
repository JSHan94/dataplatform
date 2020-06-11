<template>
  <v-col justify="center">
    <v-row>
      <v-col md="1">
        <div class="my-1">
          <v-btn large block @click="getToken">
            getToken
          </v-btn>
        </div>
      </v-col>
      <v-col md="2">
        <v-text-field label="user" outlined v-model="user"></v-text-field>
      </v-col>
      <v-col md="2">
        <v-text-field label="amount" outlined v-model="amount"></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col md="1">
        <div class="my-1">
          <v-btn large block @click="upload">
            upload
          </v-btn>
        </div>
      </v-col>
      <v-col md="2">
        <v-text-field label="fileName" outlined v-model="fileName"></v-text-field>
      </v-col>
      <v-col md="2">
        <v-text-field label="category" outlined v-model="category"></v-text-field>
      </v-col>
      <v-col md="2">
        <v-text-field label="price" outlined v-model="price"></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col md="1">
        <div class="my-1">
          <v-btn large block @click="buy">
            buy
          </v-btn>
        </div>
      </v-col>
      <v-col md="2">
        <v-text-field label="buyDatah" outlined v-model="buyDatah"></v-text-field>
      </v-col>
    </v-row>
    <!-- <v-row>
      <v-col md="1">
        <div class="my-1">
          <v-btn large block @click="getInfo">
            getInfo
          </v-btn>
        </div>
      </v-col>
    </v-row> -->
    <v-row>
      <v-col md="1">
        <div class="my-1">
          <v-btn large block @click="check">
            check
          </v-btn>
        </div>
      </v-col>
    </v-row>
    <v-row>
      <v-col md="1">
        <div class="my-1">
          <v-btn large block @click="confirm">
            confirm
          </v-btn>
        </div>
      </v-col>
      <v-col md="2">
        <v-text-field label="confirmDatah" outlined v-model="confirmDatah"></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col md="1">
        <div class="my-1">
          <v-btn large block @click="jupyter">
            jupyter
          </v-btn>
        </div>
      </v-col>
    </v-row>
  </v-col>
</template>

<script>
import axios from 'axios'
import Web3 from 'web3';
export default {
  data: () => ({
    user: '0x78658C9AaD8523BB283029C43135CF87339ADC21',
    amount: '20',
    fileName: '',
    category: '',
    price: '',
    datah: '',
    buyDatah: '',
    confirmDatah: '',
  }),
  methods:{
    getToken(){
      axios.get('http://141.223.82.142:3000/send', {
        params: {
          method: 'getToken',
          user: this.user,
          token: this.amount
        }
      })
      /*
        .then(res => {
          console.log('register-response: ', res)
        })
        .catch(err => {
          console.log('error')
        })
      */
    },
    upload(){
      axios.get('http://141.223.82.142:3000/send', {
        params: {
          method: 'uploadFile',
          category: this.category,
          fileName: this.fileName,
          price: this.price
        }
      })
      /*
        .then(res => {
          console.log('register-response: ', res)
        })
        .catch(err => {
          console.log('error')
        })
      */
    },
    buy(){
      axios.get('http://141.223.82.142:3000/send', {
        params: {
          method: 'buyFile',
          dataHash: this.buyDatah,
        }
      })
      /*
        .then(res => {
          console.log('register-response: ', res)
        })
        .catch(err => {
          console.log('error')
        })
      */
    },
    // getInfo(){
    //   axios.get('http://141.223.82.142:3000/send', {
    //     params: {
    //       method: 'getFileInformation',
    //     }
    //   })
    //   /*
    //     .then(res => {
    //       console.log('register-response: ', res)
    //     })
    //     .catch(err => {
    //       console.log('error')
    //     })
    //   */
    // },
    check(){
      axios.get('http://141.223.82.142:3000/send', {
        params: {
          method: 'checkEvent',
        }
      })
      /*
        .then(res => {
          console.log('register-response: ', res)
        })
        .catch(err => {
          console.log('error')
        })
      */
    },
    confirm(){
      axios.get('http://141.223.82.142:3000/send', {
        params: {
          method: 'salesConfirm',
          dataHash: this.confirmDatah,
        }
      })
      /*
        .then(res => {
          console.log('register-response: ', res)
        })
        .catch(err => {
          console.log('error')
        })
      */
    },
    jupyter(){
      window.location.href = "http://141.223.82.142:8080"
    }
  }
}
</script>