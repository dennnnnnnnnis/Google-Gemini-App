import { createRouter, createWebHashHistory } from "vue-router"

const routes = [
    {
        path: '/',
        component: () => import("@/views/HomePage.vue"),
    },
    {
        path: '/main-game',
        component: () => import("@/views/MainGamePage.vue"),
    },
    {
        path: '/preference',
        component: () => import("@/views/PreferencePage.vue")
    },
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router