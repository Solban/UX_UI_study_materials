import Vue from 'vue';
import VueResource from 'vue-resource';
import router from './router';
import App from './App.vue';

Vue.use(VueResource);

new Vue({
  el: '#app',
  router,
  render: h => h(App),
  http: {
    emulateJSON: true,
    emulateHTTP: true
  }
});
