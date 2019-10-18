import Vue from 'vue'
import App from './App.vue'
import Vuex from 'vuex'
import BootstrapVue from 'bootstrap-vue'
import { store } from './store.js'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import './assets/style.css'
Vue.use(BootstrapVue)
Vue.use(Vuex)

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import { faEllipsisV, faUser } from '@fortawesome/free-solid-svg-icons'
import { faSearch } from '@fortawesome/free-solid-svg-icons'
import { faStar } from '@fortawesome/free-solid-svg-icons'
import { faNewspaper } from '@fortawesome/free-solid-svg-icons'
import { faTimes } from '@fortawesome/free-solid-svg-icons'
import { faEnvelope } from '@fortawesome/free-solid-svg-icons'
import { faUserPlus } from '@fortawesome/free-solid-svg-icons'
import { faBalanceScale } from '@fortawesome/free-solid-svg-icons'
import { faExchangeAlt } from '@fortawesome/free-solid-svg-icons'
import { faUserCheck } from '@fortawesome/free-solid-svg-icons'
import { faJava } from '@fortawesome/free-brands-svg-icons'
import { faCheckSquare } from '@fortawesome/free-solid-svg-icons'
import { faSquare } from '@fortawesome/free-solid-svg-icons'
library.add(faSquare)
library.add(faCheckSquare)
library.add(faJava)
library.add(faUserCheck)
library.add(faExchangeAlt)
library.add(faBalanceScale)
library.add(faUserPlus)
library.add(faEnvelope)
library.add(faNewspaper)
library.add(faTimes)
library.add(faEllipsisV)
library.add(faSearch)
library.add(faStar)

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  store
}).$mount('#app')
