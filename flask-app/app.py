from flask import Flask, request, jsonify
from flask_cors import CORS

import google.generativeai as genai
import os
import re

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

    if len(chat.history) > 0:
        chat.rewind()
    # Generate content using the Generative Model
    response = chat.send_message(f"Hi, I want to start an interactive wording game with you. \
                      So basically it's you giving me some sentences each response \
                      on how the game is going, and ask me questions so \
                      i can make moves. Here's some basics about the game: An adventurous \
                      game with the main protagonist named {characterName} \
                      and the goal of the game being {goal}, The game difficulty should \
                      be {gameDifficulty}, i expected the interaction with me through the form \
                      of {gameType}. Examples of interaction could be asking me to choose \
                      which way to move next, or asking me to make actions in \
                      fighting with the boss etc. Now, you can start the game with few sentences \
                      on initialising of the game, like where is the protagonist, what's around him/her etc\
                      and ask me question to help you forword the game. Repeat the process, until game finished, \
                      or the goal is fulfilled. Note that i expected every response from you to be \
                      in the same structure, for instance, your response could be: (Dennis choose to go left) \
                      After 10 minutes of walk, he sees...(something something). QUESTION: What choice should you make? \
                      So the response must be in the template of (last action or choice from player or initilising of the game ), description \
                      of the effect of the action or consequences of the choice, how the game forwards, then ask question \
                      or ask me to make a move or solve a quiz or something by starting with with word 'QUESTION:'. \
                      If it's the end of the game, the {goal} goal has been reached, 'QUESTION:' should be replaced with 'THE END'. \
                      I except we hav in total of 15-40 turns based on the difficulty that I mentioned before, if it's easy, \
                      finish the game in 15-20 turns; medium, 25-30 turns; hard, 35-40 turns. The last couple turns should be about \
                      reaching the goal. Again, in the last turn or once the goal is reached, 'QUESTION:' should be replaced with 'THE END'. \
                      Note that the game must have an end. So you should control the plot of the game so that the {goal} goal can be achieved within \
                      the predetermined turns.")
    # response = model.generate_content(input_text)
    generated_text = response.text

    q_start = re.search("QUESTION:", generated_text)
    if q_start is None:
        question = ""
        description = ""
    else:
        question = generated_text[q_start.start() + 10:]
        description = generated_text[:q_start.start()]

    # Format the response
    response_data = {
        "question": question,
        "description": description
    }

    # Send the response to the front end
    return jsonify(response_data)

@app.route('/generate-answer', methods=['POST'])
def generate_answer():
    # Get the input data from the request
    data = request.json
    input_text = data.get("userInput")

    # Generate content using the Generative Model
    response = chat.send_message(input_text)
    # response = model.generate_content(input_text)
    generated_text = response.text

    q_start = re.search("QUESTION:", generated_text)
    if q_start is None:
        q_start = re.search("THE END", generated_text)
        if q_start is not None:
            question = generated_text[q_start.start():q_start.start() + 7]
            description = generated_text[:q_start.start()]
        else:
            question = ""
            description = ""
    else:
        question = generated_text[q_start.start() + 10:]
        description = generated_text[:q_start.start()]

    # Format the response
    response_data = {
        "question": question,
        "description": description
    }

    # Send the response to the front end
    return jsonify(response_data)