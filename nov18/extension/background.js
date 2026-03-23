chrome.commands.onCommand.addListener((command) => {
  console.log(`Command received: ${command}`); // Log command
  if (command === "trigger-text-fall") {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      if (tabs.length > 0) {
        chrome.scripting.executeScript({
          target: { tabId: tabs[0].id },
          files: ["content.js"]
        });
      }
    });
  }
});
