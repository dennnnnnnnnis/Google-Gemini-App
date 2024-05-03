import { defineStore } from 'pinia'
import { reactive } from 'vue'

export const useGameStageStore = defineStore('gameStage', () => {
    const steps = reactive([])
    const answers = reactive([])

    function gameNextStep(data) {
        steps.push({
            description: data["description"],
            form: {
                question: data["question"],
                answer: ""
            }
        })
    }
    function saveAnswer(index, answer){
        answer[index] = answer
    }
    function retrieveCurrStep(){
        return steps.at(-1)
    }
    return { steps, answers, gameNextStep, saveAnswer, retrieveCurrStep }
})