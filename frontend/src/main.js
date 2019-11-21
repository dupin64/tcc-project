import Vue from 'vue'
import router from './router/';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import locale from 'element-ui/lib/locale/lang/en'

import App from './App.vue';

window.axios = require('axios');
window.axios.defaults.headers.common = {
    'X-CSRFToken': window.csrfToken
};
window.axios.defaults.baseURL = 'http://localhost:8000/api/';

Vue.config.productionTip = false;
Vue.use(ElementUI, { locale });


new Vue({
    router,
    render: h => h(App)
}).$mount('#app');
