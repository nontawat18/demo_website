import Vue from 'vue'
import Vuetify from 'vuetify/lib';
import 'vuetify/dist/vuetify.min.css';

import colors from 'vuetify/es5/util/colors'

Vue.use(Vuetify, {
  theme: {
    primary: colors.red.darken1, // #E53935
    secondary: colors.red.lighten4, // #FFCDD2
    accent: colors.indigo.base // #3F51B5
  },
  iconfont: 'mdi'
})

Vue.use(Vuetify)

const opts = {}

export default new Vuetify(opts)
