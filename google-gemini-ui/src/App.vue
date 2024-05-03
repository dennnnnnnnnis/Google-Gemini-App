<template>
  <el-container class="main-layout">
    <el-header>
      <div class="header-content">
        <el-menu
          :default-active="activeIndex"
          class="el-menu-demo"
          mode="horizontal"
          background-color="transparent"
          text-color="#fff"
          active-text-color="#ffd04b"
          @select="handleSelect"
        >
          <el-menu-item index="1">Home Page</el-menu-item>
          <el-menu-item index="2">Game Page</el-menu-item>
        </el-menu>
      </div>
      <div class = "other-links">
        <el-dropdown trigger="click" @command="handleCommand">
          <el-button >
            Info<el-icon class="el-icon--right"><arrow-down /></el-icon>
          </el-button>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item command="About">About</el-dropdown-item>
              <el-dropdown-item command="Github">GitHub</el-dropdown-item>
              <el-dropdown-item command="Youtube">Youtube</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </div>
    </el-header>
    <el-main>
      <router-view/>
    </el-main>
    <el-footer 
      style="text-align: center; font-size: 20px; position: fixed; bottom: 0; width: 100%;" class="footer">© 2024 google-gemini-ui
    </el-footer>
  </el-container>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import { ArrowDown} from '@element-plus/icons-vue'
import { ref, watch } from 'vue';

const router = useRouter()
const route = useRoute();  // 使用 useRoute 钩子获取当前路由信息
const activeIndex = ref('1');  // 用 ref 创建一个响应式变量来存储活动索引

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
}, { immediate: true });  // immediate: true 确保组件加载时立即运行

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
  width: 100%; /* Ensure the menu uses the full width of its container */
  overflow: visible; /* Make sure overflow does not hide content */
}

.el-menu-item {
  min-width: 120px; /* Ensure each item has enough width to display its content */
  flex-shrink: 0; /* Prevents the menu items from shrinking */
}

.header-content {
  display: flex;
  width: 100%; /* Make sure the header content uses the full width */
  justify-content: space-between; /* Maintains space between items */
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
