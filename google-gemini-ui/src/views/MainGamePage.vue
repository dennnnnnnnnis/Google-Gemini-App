<template>
  <div class="common-layout">
    <el-container>
      <el-header style="text-align: center; font-size: 30px" class="header">Game</el-header>
      <el-main>
        <div>
          <template v-for="(item, index) in allSteps">
            <el-descriptions title="Game Stage">
              <el-descriptions-item>{{ item.description }}</el-descriptions-item>
            </el-descriptions>
            <el-form>
              <el-form-item :label="item.form.question">
                <el-input v-model="answer" type="textarea" :rows="3" placeholder="Type your answer here..."></el-input>
              </el-form-item>
              <el-button type="primary" @click="handleSubmit">Submit</el-button>
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

const handleSubmit = () => {
  let param = {
    userInput: answer.value
  }
  generateAnswer(param).then((res) => {
    console.log(res.data)
    store.gameNextStep(res.data)
    answer.value = ""
  })
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
  color: #fff; /* 文字颜色 */
}

.main {
  background-color: #E3F2FD; 
}


</style>
