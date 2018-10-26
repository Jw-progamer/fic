import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Insert from './views/Insert.vue'
import Historia from './views/Historia.vue'

Vue.use(Router)

export default new Router({
  routes: [{
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/insert',
      name: 'insert',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: Insert
    },
    {
      path: '/historia/:user',
      name: 'historia',
      component: Historia
    }
  ]
})