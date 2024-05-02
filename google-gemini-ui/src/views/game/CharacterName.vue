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
            <el-radio value="easy">Easy: 20mins</el-radio>
            <el-radio value="moderate">Moderate: 15 mins</el-radio>
            <el-radio value="hard">Hard: 10 mins</el-radio>
          </el-radio-group>
        </div>
      </el-carousel-item>
      <!-- form -->
      <el-carousel-item>
        <div class="carousel-card">
          <h3>What is your preferred interaction during the game</h3>
          <el-form label-width="auto" style="max-width: 600px">
            <el-space fill>
              <!-- 这个要想一想 -->
            <el-form-item label="Type of puzzle">
              <el-select v-model="type" placeholder="Please select what type of interaction you want">
                <el-option value="Puzzle"/>
                <el-option value="Multiple choice question" />
              </el-select>
            </el-form-item>
            <div style="max-width: 600px">
              <el-alert title="Like treasure finding, beat the boss" type="info" close-text="Gotcha" />
            </div>
            <el-form-item label="Theme of Puzzle" >
              <el-input v-model="theme" placeholder="Please type your prefered theme"></el-input>
            </el-form-item>
            </el-space>
          </el-form>
        </div>
      </el-carousel-item>
    </el-carousel>
    <div style="padding-top: 20px; text-align: center;">
      <el-button type="primary" @click="handleSubmit">Get started!</el-button>
    </div>
  </div>
</template>

<script setup>
import { gameSetup } from '@/api/api';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useGameStageStore } from '@/utils/pinia';

const selectedDifficulty = ref(''); 
const questions = ref([
  { question: 'Please enter your character name for the game:', answer: '' },
  { question: 'Please set a goal:', answer: '' },
  // Add more questions here
]);
const type = ref('');
const theme = ref('');
const router = useRouter()
const store = useGameStageStore()

const handleSubmit = () => {
  // implement the logic of submit
  console.log('Submit the data');
  let param = {
    characterName: questions.value[0]["answer"],
    goal: questions.value[1]["answer"],
    gameDifficulty: selectedDifficulty.value,
    gameType: type.value,
    theme: theme.value,
  }
  gameSetup(param).then((res) => {
    console.log(res.data)
    store.gameNextStep(res.data)
    router.push("/main-game")
  })
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
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
.el-alert {
  margin: 10px 0 0;
}
.el-alert:first-child {
  margin: 0;
}
</style>
