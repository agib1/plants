import Vue from 'vue'
import Router from 'vue-router'
import Tests from './views/Tests'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Tests',
      component: Tests
    }
  ]
})
