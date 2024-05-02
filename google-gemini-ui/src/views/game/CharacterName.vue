<template>
  <div>
    <el-carousel type="card" height="350px" :autoplay="false">
      <el-carousel-item v-for="(item, index) in questions" :key="index">
        <div class="carousel-card">
          <h3>{{ item.question }}</h3>
          <el-input v-model="item.answer" placeholder="Please type your choice"></el-input>
        </div>
      </el-carousel-item>
      <el-carousel-item>
        <div class="carousel-card">
          <h3>Please select your preferred difficulty level</h3>
          <el-radio-group v-model="selectedDifficulty">
            <el-radio value="easy">Easy</el-radio>
            <el-radio value="moderate">Moderate</el-radio>
            <el-radio value="hard">Hard</el-radio>
          </el-radio-group>
        </div>
      </el-carousel-item>
      <!-- form -->
      <el-carousel-item>
        <div class="carousel-card">
          <h3>What is your preferred interaction during the game</h3>
          <el-form label-position="top" label-width="auto" style="max-width: 600px">
            <el-space fill>
            <el-form-item label="Type of puzzle">
              <el-select v-model="type" placeholder="Please select what type of interaction you want" style="width: 360px">
                <el-option label="Puzzle" value="Puzzle"/>
                <el-option label="Multiple choice question" value="Multiple choice question" />
              </el-select>
            </el-form-item>
            </el-space>
          </el-form>
        </div>
      </el-carousel-item>
    </el-carousel>
    <div style="padding-top: 20px; text-align: center;">
      <el-button type="info" @click="handleSubmit">Get started!</el-button>
    </div>
  </div>
</template>

<script setup>
import { gameSetup } from '@/api/api';
import { ElLoading } from 'element-plus'
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useGameStageStore } from '@/utils/pinia';

const selectedDifficulty = ref(''); 
const questions = ref([
  { question: 'Please enter your character name for the game', answer: '' },
  { question: 'Please set a goal', answer: '' },
  // Add more questions here
]);
const type = ref('');
const theme = ref('');
const router = useRouter()
const store = useGameStageStore()
const isLoading = ref(false); // Loading state

const handleSubmit = async () => {
  // implement the logic of submit
  console.log('Submit the data');
  let param = {
    characterName: questions.value[0]["answer"],
    goal: questions.value[1]["answer"],
    gameDifficulty: selectedDifficulty.value,
    gameType: type.value,
    theme: theme.value,
  }
  isLoading.value = true;
  const loadingInstance = ElLoading.service({
    lock: true,
    text: 'Loading your game settings...',
    background: 'rgba(0, 0, 0, 0.7)',
  });

  // gameSetup(param).then((res) => {
  //   console.log(res.data)
  //   // store.$patch((state) => {
  //   //   state.steps.push({
  //   //     description: res.data["description"],
  //   //     form: {
  //   //         question: res.data["question"],
  //   //         answer: ""
  //   //     }
  //   //   })
  //   // })
  //   store.gameNextStep(res.data)
  //   router.push("/main-game")
  // })
  try {
    const res = await gameSetup(param);
    console.log(res.data);
    store.gameNextStep(res.data);
    router.push("/main-game");
  } catch (error) {
    console.error('Error during game setup:', error);
  } finally {
    loadingInstance.close(); // Make sure to close the loading indicator
    isLoading.value = false;
  }
}
</script>

<style scoped>
.carousel-card {
  color: #475669;
  padding: 100px;
  text-align: center;
  opacity: 0.75;
}
.el-carousel__item:nth-child(2n) {
  background-color: #bc8827;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #e8dec2;
}
.el-alert {
  margin: 10px 0 0;
}
.el-alert:first-child {
  margin: 0;
}
</style>
