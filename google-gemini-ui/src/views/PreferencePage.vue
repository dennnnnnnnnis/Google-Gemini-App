<template>
    <div class="common-layout">
      <el-container>
        <el-header style="text-align: center; font-size: 30px">Building your game</el-header>
        <el-main>
            <character-name></character-name>
        </el-main>
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

<style scoped>
.el-header {
  color: #fff; /* 文字颜色 */

}
</style>
    