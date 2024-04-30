<template>
  <div class="common-layout">
    <el-container>
      <el-header style="text-align: center; font-size: 30px">Game</el-header>
      <el-main>
        <game-description :description="steps[currentStep].description"></game-description>
        <input-dialog-form :form="steps[currentStep].form" @submit="submit"></input-dialog-form>
      </el-main>
      <el-footer style="text-align: center; font-size: 20px">© 2024 google-gemini-ui</el-footer>
    </el-container>
  </div>
</template>
  
<script>

import GameDescription from "@/views/game/GameDescription.vue";
import InputDialogForm from "@/views/game/InputDialogForm.vue";
import { defineComponent, ref, reactive } from 'vue';

export default defineComponent({
  components: {
    GameDescription,
    InputDialogForm
  },
  setup() {
    const currentStep = ref(0);
    const steps = reactive([
      {
        description: "Stage1: Backgroud",
        form: {
          question: "Are you ready to accept the challege? Please Type YES to start!",
          answer: ""
        }
      },
      {
        description: "Stage2: First Puzzle!",
        form: {
          question: "Which path you would like to choose? A or B",
          answer: ""
        }
      },
    ]);

    const submit = (answer) => {
      console.log("Current step answer:", answer);
      if (currentStep.value < steps.length - 1) {
        currentStep.value++;
      } else {
        console.log("Game setup complete!");
        // 这里可以处理游戏设置完成后的逻辑
      }
    };

    return {
      steps,
      currentStep,
      submit
    };
  },
});
</script>
    