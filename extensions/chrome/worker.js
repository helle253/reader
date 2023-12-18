import tokenPairFromCookie from './scripts/common/tokenPairFromCookie.js';

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
  chrome.contextMenus.onClicked.addListener((_, tab) => {
    chrome.scripting.executeScript({
      target: { tabId: tab.id },
      files: ['./scripts/content/synthesize.js']
    });
  });

  chrome.runtime.onMessage.addListener((message, _, __) => {
    synthesize(message.selection, message.url);
  });
}

async function synthesize(text, url) {
  const tokenPair = await tokenPairFromCookie();
  console.log("Synthesizing: " + text + " from " + url);

  fetch("http://localhost:5000/audio_clips", {
    method: "POST",
    body: JSON.stringify({
      text: text,
      source_url: url,
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
      "Authorization": `Bearer ${tokenPair?.access_token ?? ''}`
    }
  });
}
