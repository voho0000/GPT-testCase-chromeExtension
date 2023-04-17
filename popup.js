chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "showTestCase") {
      const gptGeneratedTestCase = request.testCase;
  
      // Update the test case in the popup window
      const testCaseElement = document.getElementById("test-case");
      testCaseElement.textContent = gptGeneratedTestCase;
    }
  });
  
  document.addEventListener("DOMContentLoaded", () => {
    const testCaseElement = document.getElementById("test-case");
  
    chrome.storage.local.get(["testCase"], (data) => {
      if (data.testCase) {
        testCaseElement.innerText = data.testCase;
      } else {
        testCaseElement.innerText = "No test case generated yet.";
      }
    });
  /** 
    const generateButton = document.getElementById("generate-button");
  
    generateButton.addEventListener("click", () => {
      chrome.runtime.sendMessage({
        action: "showPopup",
      });
    });*/

    const clearButton = document.getElementById("clear-button");

    clearButton.addEventListener("click", () => {
      const testCaseElement = document.getElementById("test-case");
      testCaseElement.textContent = "";
      chrome.storage.local.remove("testCase");
    });
  });
  