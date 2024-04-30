from flask import Flask, request, jsonify
from flask.views import MethodView
from flask_cors import CORS

import google.generativeai as genai
import os

os.environ['GOOGLE_API_KEY'] = "AIzaSyB6J8YW1MMgJcNhuW5lHEUSlzhypWOQ8g8"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-1.0-pro')
chat = model.start_chat()

cors = CORS()
# 用flask对象创建一个app对象
app = Flask(__name__)
cors.init_app(app)

#路由
@app.route('/') # 访问的路径
def hello():
    return 'Hello, World!'

@app.route('/game-setup', methods=['POST'])
def game_setup():
    # Get the input data from the request
    data = request.json
    characterName = data.get("characterName")
    goal = data.get("goal")
    gameDifficulty = data.get("gameDifficulty")
    gameType = data.get("gameType")
    theme = data.get("theme")

    # Generate content using the Generative Model
    chat.send_message(f"Can you give me an adventurous interactive wording game set up and basic background stuff \
                        with the main protagonist named {characterName} and the goal of the \
                        game being {goal}")
    response = chat.send_message(f"Now, based on the previous setup and background, conduct an interactive wording game. \
                                 The game difficulty should be {gameDifficulty}, the interaction with me (the player) during the \
                                 game should be conducted in {gameType} type. \
                                 Examples of interaction could be asking me to choose which way to \
                                 move next, or asking me to make actions in fighting with the boss etc. \
                                 Now, let's start the game!")
    # response = model.generate_content(input_text)
    generated_text = response.text

    # Format the response
    response_data = {'generated_text': generated_text}

    # Send the response to the front end
    return jsonify(response_data)

@app.route('/generate-answer', methods=['POST'])
def generate_answer():
    # Get the input data from the request
    data = request.json
    input_text = data.get("response")

    # Generate content using the Generative Model
    response = chat.send_message(input_text)
    # response = model.generate_content(input_text)
    generated_text = response.text

    # Format the response
    response_data = {'generated_text': generated_text}

    # Send the response to the front end
    return jsonify(response_data)