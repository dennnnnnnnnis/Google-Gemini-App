<template>
  <div class="common-layout">
    <el-container>
      <el-header style="text-align: center; font-size: 30px" class="header">Game</el-header>
      <el-main>
        <game-description :description="currStep.description"></game-description>
        <InputDialogForm :form="currStep.form"></InputDialogForm>
      </el-main>
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

// watch(() => steps, (newSteps, oldSteps) => {
//   currStep = newSteps.value.pop()
// })

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

<style>
.el-row {
  margin-bottom: 20px;
}
.el-row:last-child {
  margin-bottom: 0;
}
.el-col {
  border-radius: 4px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

.container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.header {
  color: #fff; /* 文字颜色 */
}

.main {
  background-color: #E3F2FD; 
}


</style>
