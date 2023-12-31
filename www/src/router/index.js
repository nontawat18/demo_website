import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const router = new VueRouter({
    mode: "history",
    routes: [

        {
            path: "/",
            name: "home",
            component: () =>
                import ("../views/home.vue"),
        },
        {
            path: "/dashboard",
            name: "dashboard",
            component: () =>
                import ("../views/dashboard.vue"),
        },

    ],
});

export default router;