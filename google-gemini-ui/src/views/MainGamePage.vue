<template>
  <div class="common-layout">
    <el-container>
      <el-header style="text-align: center; font-size: 30px">Game</el-header>
      <el-main>
        <game-description :description="currStep.description"></game-description>
        <InputDialogForm/>
      </el-main>
      <el-footer style="text-align: center; font-size: 20px">© 2024 google-gemini-ui</el-footer>
    </el-container>
  </div>
</template>
  
<script setup>
import GameDescription from "@/views/game/GameDescription.vue";
import InputDialogForm from "@/views/game/InputDialogForm.vue";
import { ref, reactive, watch } from 'vue';
import { useGameStageStore } from '@/utils/pinia';
import { storeToRefs } from 'pinia'
import { generateAnswer } from '@/api/api';

const store = useGameStageStore()
const { steps } = storeToRefs(store)
const currStep = steps.value.pop()

watch(() => steps, (newSteps, oldSteps) => {
  currStep = newSteps.value.pop()
})

// console.log(steps)
// console.log(currStep)

// store.$subscribe((mutation, state) => {
//   console.log(mutation)
//   console.log(state)
//   steps = state.steps
//   currStep.value = steps.value.pop()
// })

// const submit = (answer) => {
//   console.log("Current step answer:", answer);
//   let param = {
//     userInput: answer
//   }
//   generateAnswer(param).then((res) => {
//     console.log(res.data)
//     steps.push({
//       description: res.data["description"],
//       form: {
//         question: res.data["question"],
//         answer: ""
//       }
//     })
//   })
// };
</script>
    