<template>
    <div class="common-layout">
      <el-container>
        <el-header style="text-align: center; font-size: 30px">Game Preferences</el-header>
        <el-main>
            <character-name></character-name>
        </el-main>
        <el-footer style="text-align: center; font-size: 20px">© 2024 google-gemini-ui</el-footer>
      </el-container>
    </div>
</template>
  
<script>

import CharacterName from "@/views/game/CharacterName.vue"

export default {
  components: {
    CharacterName
  }
};
</script>
    