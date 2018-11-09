import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Insert from './views/Insert.vue'
import Historia from './views/Historia.vue'
import HistoriaDetail from './views/HistoriaDetail.vue'
import InsertCapitulo from './views/InsertCapitulo.vue'
import ViewHistoria from './views/ViewHistoria.vue'
import ViewCapitulo from './views/ViewCapitulo.vue'
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
      path: '/:autor/historias',
      name: 'historias',
      component: Historia,
      props: true
    },
    {
      path: '/historia/:historia_id',
      component: HistoriaDetail,
      props: true,
      children: [
        {
          path: 'add',
          name: 'add',
          component: InsertCapitulo
        },
        {
          path: '',
          name: 'historia',
          component: ViewHistoria
        }
      ]
    },
    {
      path:'/historia/:historia_id/:capitulo_id',
      name: 'capitulo',
      component: ViewCapitulo,
      props: true
    }

  ]
})
