async function sendSynthesisRequest() {
  var selection = window.getSelection().toString();
  var url = window.location.href;

  chrome.runtime.sendMessage({
    selection,
    url,
  });
}

sendSynthesisRequest();

chrome.contextMenus.onClicked.addListener(sendSynthesisRequest);
