import { createRouter, createWebHashHistory } from "vue-router"

const routes = [
    {
        path: '/main-game',
        component: () => import("@/views/MainGamePage.vue")
    },

]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router