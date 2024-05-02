<!-- <template>
    <div>
      <el-form @submit.prevent="submitGameDetails">
        <el-form-item label="Your answer">
          <el-input v-model="puzzleAnswer" placeholder="Enter your answer for the puzzle"></el-input>
        </el-form-item>
        <el-form-item label="Your choice">
          <el-input v-model="questionChoice" placeholder="Enter your choice for the question"></el-input>
        </el-form-item>
        <el-button type="primary" native-type="submit">Next!</el-button>
      </el-form>
    </div>
  </template>
  
  <script>
  import { defineComponent, ref } from 'vue';
  
  export default defineComponent({
    name: 'GameForm',
    setup() {
      const puzzleAnswer = ref('');
      const questionChoice = ref('');
  
      const submitGameDetails = () => {
        console.log('Submitted details:', { puzzleAnswer: puzzleAnswer.value, questionChoice: questionChoice.value });
        // 这里可以添加发送数据到后端的逻辑
      };
  
      return {
        puzzleAnswer,
        questionChoice,
        submitGameDetails
      };
    },
  });
  </script>
  
  <style scoped>
 
  </style>
   -->

  <template>
    <el-form @submit.prevent="handleSubmit" label-position="top">
      <el-form-item :label="form.question">
        <el-input v-model="form.answer" type="textarea" :rows="3" placeholder="Type your answer here..."></el-input>
      </el-form-item>
      <el-button type="primary" native-type="submit">Submit</el-button>
    </el-form>
  </template>
  
  <script>
  import { defineComponent, ref } from 'vue';
  
  export default defineComponent({
    props: {
      form: {
        type: Object,
        required: true
      }
    },
    setup(props, { emit }) {
      const handleSubmit = () => {
        console.log(`Submitted answer: ${props.form.answer}`);
        emit('submit', props.form.answer); // Emit the answer to the parent
      };
  
      return {
        handleSubmit
      };
    },
  });
  </script>
  
  <style scoped>
  /* Add styles here if needed */
  </style>
  