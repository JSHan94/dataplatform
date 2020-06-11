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
    </v-row>
    <v-row>
      <v-col md="1">
        <div class="my-1">
          <v-btn @click="register">
            register
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
      files: '',
      dData: '',
      name: 'test1',
      category: 'test1',
      price: '1',
    }),
  methods:{
    register(){
      let reader = new FileReader();
        reader.onload = function(e) {
        this.dData = e.target.result
        axios.post('http://141.223.82.142:3000/data', {
          'data': this.dData,
        })
        .then(res=> {
          console.log(res)
          axios.get('http://141.223.82.142:3000/send', {
          params: {
            method: 'uploadFile',
            category: this.category,
            fileName: this.fileName,
            price: this.price
          }
          })
          .then(res => {
            console.log(res)
          })
          .catch(err => {
            console.log(err)
          })
        })
        .catch(err=> {
          console.log(err)
        })
      }
      reader.readAsText(this.files[0])
    },
    onFileChange(e) {
      this.files = e.target.files || e.dataTransfer.files;
    },
  }
}
</script>