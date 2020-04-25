// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import router from './router'
import axios from 'axios'

// Vue.config.productionTip = false;
Vue.use(ElementUI);
Vue.prototype.$http = axios
Vue.prototype.$url = 'http://127.0.0.1:8000/Arxiver'

/* eslint-disable no-new */
/*new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})*/

new Vue({
	el: '#app',
	render: h => h(App),
	router
});
