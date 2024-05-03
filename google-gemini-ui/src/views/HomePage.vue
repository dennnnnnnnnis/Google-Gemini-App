<template>
  <div class="background" :style="{ height: 'calc(100vh - 68px)' }">
    <div class="background-color" style="background-color: rgba(0, 0, 0, 0.8);"></div>
    <div class="text text-center">
      <div class>
        <h1 class="">Welcome to the <span class="text-gemini">D&H 80s text-adventure</span> Game</h1>
        <p class="">Build your own retro text game and play!</p>
        <div style="display: flex; flex-wrap: wrap; gap: 16px; justify-content: center; align-items: center;">
          <el-button type="primary" @click="goToGame">Get started</el-button>
        </div>
      </div>
    </div>
  </div>
</template>
  
<script setup>

import { useRouter } from 'vue-router';

const router = useRouter();


function goToGame() {
  router.push('/preference');
}
</script>
  
<style scoped>

.backgroud-color {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

.text {
  position: relative;
  padding: 150px;
  color: #ffffff; /* assuming text-neutral-content is white */
  font-size: 2rem;
}

.text-center {
  text-align: center;
}

</style>