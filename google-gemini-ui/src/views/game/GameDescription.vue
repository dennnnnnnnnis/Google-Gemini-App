<template>
  <el-descriptions title="Game Stage">
    <el-descriptions-item>{{ description }}</el-descriptions-item>
  </el-descriptions>
</template>

<script>
export default {
  props: ['description']
}
</script>


<!-- 
<script>
import { defineComponent, ref } from 'vue';

export default defineComponent({
  name: 'GamePage',
  setup() {
    const dialogVisible = ref(false); // 控制对话框的显示
    const characterName = ref(''); // 存储角色名称
    const gameObjective = ref(''); // 存储游戏目标

    const handleClose = () => {
      console.log('Dialog closed');
    };
    const handleClose = (done: () => void) => {
        ElMessageBox.confirm('Are you sure to close this dialog?')
        .then(() => {
        done()
        })
        .catch(() => {
        // catch error
        })
    }

    const submitGameDetails = () => {
      console.log('Submitted details:', { characterName: characterName.value, gameObjective: gameObjective.value });
      dialogVisible.value = false; // 关闭对话框
      // 在此处添加发送到后端的代码
    };

    return {
      dialogVisible,
      characterName,
      gameObjective,
      handleClose,
      submitGameDetails
    };
  },
});
</script>

<style scoped>
.dialog-footer {
  text-align: right;
}
</style>

   -->