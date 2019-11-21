import Vue from 'vue';
import Router from 'vue-router';

//components
import Dashboard from '../components/Dashboard.vue';
import Specialists from '../components/Specialists.vue';

Vue.use(Router);

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            alias: '/dashboard',
            name: 'dashboard',
            component: Dashboard
        },
        {
            path: '/specialists',
            name: 'specialists',
            component: Specialists
        }
    ]
});
