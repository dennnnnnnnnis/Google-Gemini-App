from flask import Flask, request, jsonify
from flask.views import MethodView
from flask_cors import CORS

import google.generativeai as genai
import os

os.environ['GOOGLE_API_KEY'] = "AIzaSyB6J8YW1MMgJcNhuW5lHEUSlzhypWOQ8g8"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-1.0-pro')

cors = CORS()
# 用flask对象创建一个app对象
app = Flask(__name__)
cors.init_app(app)

#路由
@app.route('/') # 访问的路径
def hello():
    return 'Hello, World!'

@app.route('/generate', methods=['POST'])
def generate_content():
    # Get the input data from the request
    data = request.json
    input_text = data.get("response")

    # Generate content using the Generative Model
    response = model.generate_content(input_text)
    generated_text = response.text

    # Format the response
    response_data = {'generated_text': generated_text}

    # Send the response to the front end
    return jsonify(response_data)