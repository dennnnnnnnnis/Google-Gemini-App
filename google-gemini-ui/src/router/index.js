import { createRouter, createWebHashHistory } from "vue-router"

const routes = [
    {
        path: '/preference',
        component: () => import("@/views/PreferencePage.vue")
    },
    {
        path: "/language",
        component: () => import("@/views/game/SetLanguage.vue")
    },

]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router