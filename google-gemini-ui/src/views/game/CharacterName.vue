
<template>
  <div>
    <el-carousel type="card" height="300px" :autoplay="false">
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
            <el-radio label="easy">Easy: 20mins</el-radio>
            <el-radio label="moderate">Moderate: 15 mins</el-radio>
            <el-radio label="hard">Hard: 10 mins</el-radio>
          </el-radio-group>
        </div>
      </el-carousel-item>
      <!-- form -->
      <el-carousel-item>
        <div class="carousel-card">
          <h3>What is your preferred interaction during the game</h3>
          <el-form>
            <!-- 这个要想一想 -->
            <el-form-item label="Type of puzzle">
              <el-select v-model="type" placeholder="Please select what type you want to choose">
                <el-option label="Puzzle"/>
                <el-option label="Multiple choice question" />
              </el-select>
            </el-form-item>
            <el-form-item label="Theme of Puzzle">
              <el-input v-model="age"></el-input>
            </el-form-item>
          </el-form>
        </div>
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue';

export default defineComponent({
  name: 'MyCarousel',
  setup() {
    const selectedDifficulty = ref(''); 
    const handleDifficultyChange = (value) => {
      console.log('Selected difficulty:', value);
    };

    const questions = ref([
      { question: 'Please enter your character name for the game:', answer: '' },
      { question: 'Please set a goal:', answer: '' },
      // Add more questions here
    ]);
    const type = ref('');
    return {
      questions,
      selectedDifficulty,
      handleDifficultyChange,
      type,
    };
    
  },
});
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
</style>
