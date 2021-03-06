import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/Register',
    name: 'Register',
    component: () => import('../views/Register.vue')
  },
  {
    path: '/Product',
    name: 'Product',
    component: () => import('../views/Product.vue')
  },
  {
    path: '/ProductInfo/:id',
    name: 'ProductInfo',
    component: () => import('../views/ProductInfo.vue')
  },
  {
    path: '/MyPage',
    name: 'MyPage',
    component: () => import('../views/MyPage.vue')
  },
  {
    path: '/Userinfo',
    name: 'Userinfo',
    component: () => import('../views/Userinfo.vue')
  },
  {
    path: '/Temp',
    name: 'Temp',
    component: () => import('../views/Temp.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
