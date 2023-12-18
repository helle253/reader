

chrome.runtime.onMessage.addListener((msg, __, sendResponse) => {
  if (msg.type === 'synthesize') {
    var selection = window.getSelection().toString();
    var url = window.location.href;

    sendResponse({
      selection,
      url,
    });
  }
});
