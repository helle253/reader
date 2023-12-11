chrome.runtime.onInstalled.addListener(function () {
  chrome.contextMenus.create(
    {
      title: "Copy to Colab",
      contexts: ['selection'],
      id: 'selection',
    },
  );

  chrome.contextMenus.onClicked.addListener((info, _tab) => {
    openColab(info.selectionText)
  })
});

function openColab(text) {
  console.log("Opening Colab with the following snippet:" + text)
}