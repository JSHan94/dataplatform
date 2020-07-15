<template>
  <v-container>
    <v-row justify="center">
      <v-col md="7">
        <v-text-field v-model="name" label="File Name" outlined></v-text-field>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col md="7">
        <v-text-field v-model="price" label="Price" outlined></v-text-field>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col md="7">
        <v-select :items="categories" v-model="category" label="Category" outlined></v-select>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col md="7">
        <v-file-input show-size label="File" outlined prepend-icon v-model="files"></v-file-input>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col md="7">
        <v-btn block large color="primary" @click="register(name, category, price)">
          register
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'
import Web3 from 'web3';

export default {
  data: () => ({
      files: null,
      dData: '',
      name: '',
      category: '',
      categories: ['Blockchain', 'Health', 'Money', 'Device', 'Weather'],
      price: '',
    }),
  methods:{
    register(name, category, price){
      let reader = new FileReader();
        reader.readAsText(this.files)
        reader.onload = function(e) {
        this.dData = e.target.result
        axios.post('http://141.223.82.142:3000/data', {
          'data': this.dData,
        })
        .then(() => {
          axios.get('http://141.223.82.142:3000/send', {
            params: {
              method: 'uploadFile',
              category: category,
              fileName: name,
              price: price
            }
          })
          .then(res => {
          })
          .catch(err => {
            console.log(err)
          })
        })
        .catch(err=> {
          console.log(err)
        })
        alert('등록이 완료되었습니다.')
      }
    },
  }
}
</script>