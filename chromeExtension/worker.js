chrome.runtime.onInstalled.addListener(function () {
  chrome.contextMenus.create(
    {
      title: "Synthesize",
      contexts: ['selection'],
      id: 'selection',
    },
  );

  chrome.contextMenus.onClicked.addListener((info, _tab) => {
    synthesize(info.selectionText)
  })
});

function synthesize(text) {
  console.log("Synthesizing with the following snippet:" + text)
}
