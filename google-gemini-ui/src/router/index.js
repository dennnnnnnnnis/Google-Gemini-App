import { createRouter, createWebHashHistory } from "vue-router"

const routes = [
    {
        path: '/main-game',
        component: () => import("@/views/MainGamePage.vue"),
    },
    {
        path: '/preference',
        component: () => import("@/views/PreferencePage.vue")
    },
    {
        path: '/language',
        component: () => import("@/views/SetLanguage.vue")
    },
    {
        path: '/test',
        component: () => import("@/views/game/GameTest.vue")
    },

]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router