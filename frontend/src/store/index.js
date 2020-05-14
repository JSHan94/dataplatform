import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    Links: [
      {
        name: 'Home',
        routerName: 'Home'
      },
      {
        name: 'Register',
        routerName: 'Register'
      },
      {
        name: 'Product',
        routerName: 'Product'
      },
      {
        name: 'Temp',
        routerName: 'Temp'
      }
    ],
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
