import { defineStore } from 'pinia'
import { reactive } from 'vue'

export const useGameStageStore = defineStore('gameStage', () => {
    const steps = reactive([])

    function gameNextStep(data) {
        steps.push({
            description: data["description"],
            form: {
                question: data["question"],
                answer: ""
            }
        })
    }
    function retrieveCurrStep(){
        return steps.at(-1)
    }
    return { steps, gameNextStep, retrieveCurrStep }
})