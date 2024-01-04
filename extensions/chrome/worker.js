chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create(
    {
      title: "Synthesize",
      contexts: ['selection'],
      id: 'selection',
    }
  );

  initializeListeners();
});

chrome.runtime.onStartup.addListener(initializeListeners);

function initializeListeners() {
  chrome.contextMenus.onClicked.addListener(async (_, tab) => {
    await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      files: ['./scripts/content/synthesize.js']
    })

    chrome.tabs.sendMessage(tab.id, {type: 'synthesize'}, (response) => {
      synthesize(response.selection, response.url);
    });
  });
}

async function synthesize(text, url) {
  console.log("Synthesizing: " + text + " from " + url);

  fetch("http://localhost:5000/audio_clips", {
    method: "POST",
    body: JSON.stringify({
      text: text,
      source_url: url,
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    }
  });
}
