import { createRouter, createWebHashHistory } from "vue-router"

const routes = [
    {
        path: '/test',
        component: () => import("@/views/game/GameTest.vue")
    },
    {
        path: '/play',
        component: () => import("@/views/game/GameList.vue")
    },

]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router