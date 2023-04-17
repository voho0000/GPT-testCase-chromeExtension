from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import openai
import requests
import json
from dotenv import load_dotenv
import os

# Load the .env file located in the 'config' directory
load_dotenv()
AZURE_API_KEY = os.getenv('AZURE_API_KEY')

openai.api_type = "azure"
# replace with you api endpoint
openai.api_base = "https://YourOwn-OpenAI-EndPoint.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = AZURE_API_KEY

app = Flask(__name__)
CORS(app)


@app.route('/generate_test_case', methods=['POST'])
@cross_origin()
def generate_test_case():
    defect_description = request.json['defect_description']

    # Call GPT-3 API with the defect_description
    prompt = f"請用台灣繁體中文回答問題，利用以下defect描述產出對應的測試案例: {defect_description}"
    print(prompt)

    response = openai.Completion.create(
        engine="gpt-35-turbo",
        prompt=prompt,
        temperature=0.3,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)
    test_steps = response['choices'][0]['text'].strip()

    print(test_steps)

    return jsonify(test_steps=test_steps)


if __name__ == '__main__':
    app.run()
