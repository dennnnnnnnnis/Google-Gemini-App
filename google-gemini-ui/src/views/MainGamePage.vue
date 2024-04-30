<template>
    <div class="common-layout">
      <el-container>
        <el-header style="text-align: center; font-size: 30px">Game Preferences</el-header>
        <el-main>
            <main-game></main-game>
        </el-main>
        <el-footer style="text-align: center; font-size: 20px">© 2024 google-gemini-ui</el-footer>
      </el-container>
    </div>
  </template>
  
  <script>

//   import { ElInput, ElButton } from 'element-plus'; // Make sure to import these if they are not globally registered
  import MainGame from "@/views/game/MainGame.vue"

 export default {
  components: {
    MainGame 
  }
};
</script>
    