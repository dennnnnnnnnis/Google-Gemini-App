<template>
  <div class="common-layout">
    <el-container>
      <el-header style="text-align: center; font-size: 30px" class="header">Game</el-header>
      <el-main class="main-content">
        <div>
          <template v-for="(item, index) in allSteps">
            <el-descriptions title="Game Stage">
              <el-descriptions-item>{{ item.description }}</el-descriptions-item>
            </el-descriptions>
            <div v-if="completedStages.has(index)">
              <p>{{ item.form.question }}</p >
              <p>{{ store.answers[index] }}</p > <!-- Display the stored answer -->
            </div>
            <el-form v-else>
              <el-form-item :label="item.form.question">
                <el-input v-model="answer" type="textarea" :rows="3" placeholder="Type your answer here..."></el-input>
              </el-form-item>
              <el-button type="primary" @click="() => handleSubmit(index)">Submit</el-button>
            </el-form>
          </template>
        </div>
      </el-main>
    </el-container>
  </div>
</template>
  
<script setup>
import { ref, computed } from 'vue';
import { useGameStageStore } from '@/utils/pinia';
import { generateAnswer } from '@/api/api';

const store = useGameStageStore()
const answer = ref("")
const completedStages = ref(new Set());

const handleSubmit = () => {
  let param = {
    userInput: answer.value
  }
  generateAnswer(param).then((res) => {
    console.log(res.data)
    store.saveAnswer(index, answer.value)
    store.gameNextStep(res.data)
    completedStages.value.add(index)
    answer.value = ""
  }) .catch(error =>{
    console.log("Error submitting the answer:", error)
  });
};

const allSteps = computed(() => store.steps);
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
  color: #ffffff; 
  font-size:larger
}

.main-content {
  background-color: rgba(175, 113, 47, 0.9);
  /* background-color: #E3F2FD;  */
}


</style>
