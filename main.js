import App from './App'
import uView from "uview-ui";

// #ifndef VUE3
import Vue from 'vue'
import './uni.promisify.adaptor'

import pageSearch from '@/components/pageSearch/pageSearch.vue'
import mineNavbar from '@/components/mineNavbar/mineNavbar.vue'
import mineTabbar from '@/components/mineTabbar/mineTabbar.vue'
import militaryGeneral from '@/components/militaryGeneral/militaryGeneral.vue'

Vue.use(uView);
Vue.component('page-search', pageSearch);
Vue.component('mine-navbar', mineNavbar);
Vue.component('mine-tabbar', mineTabbar);
Vue.component('military-general', militaryGeneral);
Vue.config.productionTip = false
App.mpType = 'app'
const app = new Vue({
	...App
})
app.$mount()
// #endif

// #ifdef VUE3
import {
	createSSRApp
} from 'vue'
export function createApp() {
	const app = createSSRApp(App)
	return {
		app
	}
}
// #endif