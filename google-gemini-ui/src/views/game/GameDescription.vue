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

