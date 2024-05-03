# Google-Gemini-App

This project is created as part of the [Google AI Hackthon](https://googleai.devpost.com).

This project aims to bring the adventurous wording games from 90s and 00s back to the current generation. It allows users to enter their preferences on the goal of the game, character of the game, and the form of interactions etc. Then a vintage, nostalgic adventurous wording game is created, user can make actions and responses based on the given scenarios or different situations, giving them a unique experience apart from all the technologies used nowadays.

# Backend
The backend infrastructure is built with RestAPI and Python, based on a Flask framework.

# Frontend
The frontend is powered by Vue 3 (compositional API), supported by element-plus for component library.

# Summary
The Google Gemini AI model is embedded into the backend development, the backend will send responses to the frontend generated from the model (LLM), with the settings and preferences entered by the user in the preference page. These settings act as components of a prompt and the prompt will act as an input to the model so that the model can give reponses interactively based on user's input.

# Future improvements
Some improvements are possible mainly for the UI of the game page:
- Dynamic chat boxes containing description and user's response of the current step (stage) of the game.
- The display settings of the words and chat boxes in the game page, Especially the colour and the font of the texts.
- More dynamic interactions between components, however, for the sake of the game, this might not be conducted as the app is a wording game, the style overall should be simple, vintage, easy and 90s, no further fancy rendering should be required.

# Run
- Intall the required dependencies in [google-gemini-ui](https://github.com/dennnnnnnnnis/Google-Gemini-App/tree/main/google-gemini-ui) repository
    ```npm install```
- Then intall the required dependency for running both frontend and backend concurrently (note that you need to cd to the root directory first)
    ```npm install concurrently --save-dev```
- Now everything is clear and good to go, try run ``` npm start ``` (Again, cd to the root directory)
