<template>
  <div class="common-layout">
    <el-container class="container">
      <el-header style="text-align: center; font-size: 30px" class="header">Game</el-header>
      <el-main class="main">
        <el-row :gutter="20">
          <el-col :span="16"><game-description :description="steps[currentStep].description"></game-description></el-col>
          <!-- 这里应该是之前的input -->
          <el-col :span="8"><input-dialog-form :form="steps[currentStep].form" @submit="submit"></input-dialog-form></el-col>
        </el-row>
        <el-row>
          <el-col :span="24"><input-dialog-form :form="steps[currentStep].form" @submit="submit"></input-dialog-form></el-col>
        </el-row>
      </el-main>
      <el-footer style="text-align: center; font-size: 20px; position: fixed; bottom: 0; width: 100%;" class="footer">© 2024 google-gemini-ui</el-footer>
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
  background-color: #283593; /* 深蓝色 */
  color: #fff; /* 文字颜色 */
}

.main {
  background-color: #E3F2FD; /* 浅蓝色 */
}

.footer {
  background-color: #283593; /* 深蓝色 */
  color: #fff; /* 文字颜色 */
}
</style>
