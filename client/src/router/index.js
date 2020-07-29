import Vue from 'vue';
import Router from 'vue-router';
import MainInfo from '@/components/MainInfo';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'MainInfo',
      component: MainInfo,
    },
  ],
});
