document.addEventListener("DOMContentLoaded", loadState);

document.getElementById("clickMe").addEventListener("click", myFunction);

let host = "http://localhost:5000"
var tokenPair;

async function loadState() {
  const cookie = await chrome.cookies.get({url: host, name: "tokenPair"});
  tokenPair = JSON.parse(cookie.value || '{}');
}

function myFunction(){
  console.log('clicked!');
}
