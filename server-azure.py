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
# openai.api_version = "2022-12-01"
openai.api_version = "2023-03-15-preview" 
openai.api_key = AZURE_API_KEY

app = Flask(__name__)
CORS(app)


@app.route('/generate_test_case', methods=['POST'])
@cross_origin()
def generate_test_case():
    defect_description = request.json['defect_description']
    prompt_prefix = request.json["prompt_prefix"]
    # Call GPT-3 API with the defect_description
    prompt = f"{prompt_prefix} {defect_description}"
    print(prompt)

    response = openai.ChatCompletion.create(
        engine="gpt-35-turbo", 
        messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ],
        temperature=0.5,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)
    
    test_steps = response['choices'][0]['message']['content'].strip()

    print(test_steps)

    return jsonify(test_steps=test_steps)


if __name__ == '__main__':
    app.run()
