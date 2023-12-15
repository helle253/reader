var selection = window.getSelection().toString();
var url = window.location.href;

chrome.runtime.sendMessage({selection, url});
