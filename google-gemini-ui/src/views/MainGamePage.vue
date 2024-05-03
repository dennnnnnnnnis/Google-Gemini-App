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
            <el-form>
              <el-form-item :label="item.form.question" class="word-display">
                <div v-if="item.form.answer.length>0">
                  <el-text class="mx-1" size="large">{{ item.form.answer }}</el-text>
                </div>
                <div v-else>
                  <div v-if="item.form.question === 'THE END'">
                    <el-dialog
                      v-model="dialogVisible"
                      title=""
                      width="500"
                      :open-delay=5000
                    ></el-dialog>
                  </div>
                  <div v-else>
                    <el-input v-model="answer" type="textarea" :rows="3" placeholder="Type your answer here..."></el-input>
                  </div>
                </div>
              </el-form-item>
              <div class="el-right">
                <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png" class="avatar" />
                <el-button type="primary" @click="handleSubmit" class="submit-button">Submit</el-button>
              </div>
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
const dialogVisible = ref(true)

const handleSubmit = () => {
  let param = {
    userInput: answer.value
  }
  generateAnswer(param).then((res) => {
    console.log(res.data)
    store.saveAnswer(answer.value)
    store.gameNextStep(res.data)
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

.el-right {
  display: flex;
  align-items: center;
  justify-content: right;
}

.avatar {
  margin-left: 20px;
}

.submit-button {
  margin-left: 20px;
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

.word-display {
  color:rgb(247, 246, 242);
  font-size:x-large
}


</style>
