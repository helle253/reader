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

function synthesize(text, url) {
  fetch("http://localhost:5000/audio_clips", {
    method: "POST",
    body: JSON.stringify({
      text: text,
      source_url: url,
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8"
    }
  });
}
