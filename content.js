chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'getSelectedText') {
      const selectedText = window.getSelection().toString();
      const promptPrefix = document.getElementById("prompt-prefix").value;
      // Update the test case in the popup window
      //document.getElementById("selected-text").textContent = selectedText;

      fetch('http://127.0.0.1:5000/generate_test_case', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
          defect_description: selectedText,
          promptPrefix: promptPrefix
         }),
      })
        .then((response) => response.json())
        .then((data) => {
          // Store the received test case in the local storage
          chrome.storage.local.set({ testCase: data.test_steps });
  
          // Send a message back to the background script to show the test case in the popup
          chrome.runtime.sendMessage({
            action: 'showTestCase',
            testCase: data.test_steps,
          });
        })
        .catch((error) => {
          console.error('Error fetching test case:', error);
        });
    }
  });
  