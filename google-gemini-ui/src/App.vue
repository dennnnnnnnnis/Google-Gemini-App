<template>
  <el-container class="main-layout">
    <el-header>
      <div class="header-content">
        <el-menu
          :default-active="activeIndex"
          class="el-menu-demo"
          mode="horizontal"
          background-color="transparent"
          text-color="#000000"
          active-text-color="#ffd04b"
          @select="handleSelect"
        >
          <el-menu-item index="1"><el-icon><Eleme /></el-icon>Home Page</el-menu-item>
          <el-menu-item index="2"><el-icon><Setting /></el-icon>Setting Page</el-menu-item>
          <el-menu-item index="3" disabled><el-icon><SwitchFilled /></el-icon>Game Page</el-menu-item>
        </el-menu>
      </div>
      <div class = "other-links">
        <el-dropdown trigger="click" @command="handleCommand">
          <el-button >
            Info<el-icon class="el-icon--right"><arrow-down /></el-icon>
          </el-button>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item command="About"><el-icon><Document /></el-icon>About</el-dropdown-item>
              <el-dropdown-item command="Github"><el-icon><Platform /></el-icon>GitHub</el-dropdown-item>
              <el-dropdown-item command="Youtube"><el-icon><VideoPlay /></el-icon>Youtube</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </div>
    </el-header>
    <el-main>
      <router-view/>
    </el-main>
    <el-footer 
      style="text-align: center; font-size: 20px; position: fixed; bottom: 0; width: 100%;" class="footer">© 2024 google-gemini (UI still to be updated...)
    </el-footer>
  </el-container>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import { ArrowDown } from '@element-plus/icons-vue'
import { ref, watch } from 'vue';
import { VideoPlay, Platform, Setting, Document, SwitchFilled, Eleme } from '@element-plus/icons-vue';

const router = useRouter()
const route = useRoute(); 
const activeIndex = ref('1'); 

watch(route, (newRoute) => {
  switch (newRoute.path) {
    case '/':
      activeIndex.value = '1';
      break;
    case '/preference':
      activeIndex.value = '2';
      break;
    // 添加其他路由匹配
  }
}, { immediate: true });

function handleSelect(index) {
  // Navigation logic based on selected menu index
  switch (index) {
    case '1':
      router.push('/');
      break;
    case '2':
      router.push('/preference');
      break;
  }
}
function handleCommand(command) {
  // Handles actions for dropdown commands
  switch (command) {
    case 'About':
      console.log('Action 1 executed');
      router.push('/about');
      break;
    case 'Github':
      console.log('Action 2 executed');
      window.open('https://github.com/dennnnnnnnnis/Google-Gemini-App', '_blank');
      break;
    case 'Youtube':
      console.log('Action 3 executed');
      break;
  }
}
</script>


<style scoped>
.el-menu {
  width: 100%; 
  overflow: visible; 
}

.el-menu-item {
  min-width: 120px; 
  flex-shrink: 0; 
}

.header-content {
  display: flex;
  width: 100%; 
  justify-content: space-between;
}

.other-links{
  display: flex;
  width: 10%; 
  justify-content: space-between; 
}

header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

.el-header, .el-footer {
  background-color: #333;
  background-image: linear-gradient(45deg, #dfcbae, #704114); /* Sample gradient pattern */
  color: #704114;
  text-align: center;
  padding: 10px 50px; /* Adjust padding as needed */
}

.el-main {
  background-color: #fff;
  background-image: url('@/assets/backgroundimage.jpg'); /* Add your background image path */
  background-size: cover;
  background-position: center;
  min-height: calc(100vh - 120px); /* Adjust based on header and footer height */
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
