from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import openai
import requests
import json
from dotenv import load_dotenv
import os

# Load the .env file located in the project directory
load_dotenv()
AZURE_API_KEY = os.getenv('AZURE_API_KEY')

openai.api_type = "azure"
# replace with you api endpoint
openai.api_base = "https://YourOwn-OpenAI-EndPoint.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = AZURE_API_KEY

app = Flask(__name__)
CORS(app)


@app.route('/generate_test_case', methods=['POST'])
@cross_origin()
def generate_test_case():
    defect_description = request.json['defect_description']

    # Call GPT-3 API with the defect_description
    prompt = f"請用台灣繁體中文回答問題，利用以下系統缺陷描述產出對應的測試案例: {defect_description}"
    print(prompt)

    # If you use a GPT-3 series model, use the following code to call api
    '''
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)
    test_steps = response['choices'][0]['text'].strip()
    '''

    # If you use GPT 3.5 or GPT 4, use the following code to call api
    response = openai.ChatCompletion.create(
        engine="gpt-35-turbo",  # engine="gpt-4",
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
