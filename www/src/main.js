import Vue from "vue";
import { createPinia, PiniaVuePlugin } from "pinia";
import App from "./App.vue";
import router from "./router";
import store from './stores/cart';
import './axios'

import vuetify from '@/plugins/vuetify'
import Vuetify from "vuetify";
import "vuetify/dist/vuetify.min.css";
import '@mdi/font/css/materialdesignicons.css';
import 'material-design-icons-iconfont/dist/material-design-icons.css';

import Swiper, { Navigation, Pagination } from 'swiper';
// import Swiper and modules styles
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';

import "./assets/main.css";



Vue.use(vuetify, {
    iconfont: ['mdi', 'fa']
})


Vue.use(Vuetify);
Vue.use(PiniaVuePlugin);

const swiper = new Swiper('.swiper', {
    // configure Swiper to use modules
    modules: [Navigation, Pagination],
})

new Vue({
    router,
    vuetify,
    store,
    pinia: createPinia(),
    render: (h) => h(App),
}).$mount("#app");