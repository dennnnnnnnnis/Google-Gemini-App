import { defineStore } from 'pinia'
import { reactive } from 'vue'

export const useGameStageStore = defineStore('gameStage', () => {
    const steps = reactive([])
    // const answers = reactive([])

    function gameNextStep(data) {
        steps.push({
            description: data["description"],
            form: {
                question: data["question"],
                answer: ""
            }
        })
    }
    function saveAnswer(answer){
        steps.at(-1).form.answer = answer
        // answers.push(answer)
    }
    function retrieveCurrStep(){
        return steps.at(-1)
    }
    function clearGame(){
        if (steps.length > 0){
            steps.pop()
        }
    }
    return { steps, gameNextStep, saveAnswer, retrieveCurrStep, clearGame }
})