<template>
    <div class="main-content">
      <h1>D&H text-adventure in 80s</h1>
      
      <section>
        <h2>What is this game</h2>
        <p>This project introduces a retro-style word game that capitalizes on the capabilities of the Google Gemini API to create an engaging and interactive user experience. By leveraging this advanced API, the game allows users to craft their own unique gameplay scenarios and challenges. The Google Gemini API plays a crucial role, generating both the game's descriptions and the subsequent questions that prompt users for their next move, ensuring a dynamic and ever-evolving gameplay.
The essence of this game lies in its nostalgic appeal, offering a vintage, old-school vibe that is designed to evoke childhood memories and bring a touch of nostalgia to modern gaming. Players are transported back in time through a simple yet captivating word-based gameplay that challenges their creativity and quick thinking.

To further enhance the user experience, the project proposes optional improvements through the integration of large language models (LLMs). These models could be used to refine the game's linguistic capabilities, such as improving the complexity and relevance of the questions asked or expanding the descriptive elements within the game. This integration not only advances the technical sophistication of the game but also enriches the interactive elements, making for a more immersive and personalized gaming experience.

Overall, this retro word game merges traditional gameplay elements with modern technological advancements, offering both a tribute to the past and a step towards the future of interactive entertainment.</p>
      </section>
  
      <section>
        <h2>Backend</h2>
        <p>The backend infrastructure is built with RestAPI and Python, based on a Flask framework.</p>
      </section>
  
      <section>
        <h2>Frontend</h2>
        <p>The frontend is powered by Vue 3 (compositional API), supported by element-plus for component library.</p>
      </section>

    </div>
  </template>
  
  <style scoped>
  .about-container {
    margin: 20px;
    font-family: Arial, sans-serif;
  }
  h1, h2 {
    color: #333;
  }
  p {
    color: #666;
    line-height: 1.6;
  }
  .main-content {
  background-color: rgba(175, 113, 47, 0.9);
  /* background-color: #E3F2FD;  */
}
  </style>
  