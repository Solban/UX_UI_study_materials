import Vue from 'vue';
import Router from 'vue-router';
import Home from './components/Home.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/:category',
      name: 'Category',
      component: Home
    },
    {
      path: '/:category/:id',
      name: 'Example',
      component: Home
    }
  ]
});

