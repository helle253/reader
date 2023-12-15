import tokenPairFromCookie from './scripts/common/tokenPairFromCookie.js'

chrome.runtime.onInstalled.addListener(function () {
  chrome.contextMenus.create(
    {
      title: "Synthesize",
      contexts: ['selection'],
      id: 'selection',
    },
  );

  chrome.contextMenus.onClicked.addListener((info, tab) => {
    synthesize(info.selectionText, tab.url)
  })
});

async function synthesize(text, url) {
  tokenPair = await tokenPairFromCookie();
  console.log("Synthesizing: " + text + " from " + url);

  fetch("http://localhost:5000/audio_clips", {
    method: "POST",
    body: JSON.stringify({
      text: text,
      source_url: url,
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
      "Authorization": `Bearer ${tokenPair.access_token}`
    }
  });
}
