# Test Case Generator Chrome Extension

This Chrome extension uses GPT-3.5 Turbo to generate test cases based on selected defect descriptions. The extension adds a context menu item to generate test cases when text is selected on a web page.

## Features

- Generate test cases based on selected defect descriptions
- Display generated test cases in a popup
- Clear generated test cases

## Demo
Check out the demo video of the Test Case Generator Chrome extension in action. Please note that there is a 20-second waiting period for GPT to complete the test case generation.
![demo](https://user-images.githubusercontent.com/39255863/232571004-79833bad-cbb7-4313-8ada-2a97da59ccd2.gif)


## Installation

1. Clone this repository

2. Navigate to the project directory:
`cd GPT-testCase-chromeExtension`

3. Install required Python packages:
`pip install -r requirements.txt`

4. Create a `.env` file in the root directory of the project and add your OpenAI API key:
`OPENAI_API_KEY = xxxxxx`

5. Run the Flask server:
- openai endpoint
`python server.py`
- azure endpoint (need to replace default endpoint to your own endpoint)
`python server-azure.py` 

6. If your Flask server is not hosted on port 5000, add the Flask hosting URL to the host_permissions in the manifest.json file

7. Load the Chrome extension:
    - Open the Chrome browser and navigate to `chrome://extensions/`.
    - Enable "Developer mode" using the toggle in the top right corner.
    - Click "Load unpacked" and select the project directory.


## Usage

1. Select a defect description text on a web page.

2. Right-click the selected text and choose "Generate Test Case" from the context menu.

3. The generated test case will be displayed in a popup.

4. Click the "Clear Test Case" button to clear the displayed test case.

## Dependencies

- GPT-3.5 Turbo API
- Flask (for the server-side component)

## License

MIT License
