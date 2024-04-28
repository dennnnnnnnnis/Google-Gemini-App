<template>
    <div class="language-settings">
        <el-form :model="form" label-width="auto" style="max-width: 600px">
            <el-form-item label="Language setting">
                <el-select v-model="form.region" placeholder="Please select your prefered language!">
                    <el-option label="English" value="English" />
                    <el-option label="简体中文" value="Chinese" />
                    <el-option label="한국어" value="Korean" />
                    <el-option label="日本語" value="Japanese" />
                </el-select>
            </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="onSubmit">Create</el-button>
            <el-button>Cancel</el-button>
        </el-form-item>
        </el-form>
    </div>
</template>
  
<script setup>
import { reactive } from 'vue'

// do not use same name with ref
const form = reactive({
region: '',
type: [],
})
const onSubmit = () => {
console.log('submit!')
}
</script>

<style>
.language-settings {
  padding: 20px;
  background-color: #f8f9fa; 
  border-radius: 8px; 
  box-shadow: 0 2px 12px rgba(0,0,0,0.1); 
  margin: auto; 
  max-width: 800px; 
}
</style>
  