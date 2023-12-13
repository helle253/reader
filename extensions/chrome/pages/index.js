document.addEventListener("DOMContentLoaded", loadState);

let host = "http://localhost:5000"
var tokenPair;

async function loadState() {
  const cookie = await chrome.cookies.get({url: host, name: "tokenPair"});
  if (cookie && cookie.value) {
    try {
      tokenPair = JSON.parse(cookie.value);
    } catch (e) {
      console.error("Error parsing tokenPair cookie.");
    }
  }

  initializeUI(!!tokenPair)
}

function initializeUI(isLoggedIn) {
  if (isLoggedIn) {
    document.getElementById("logout").removeAttribute("hidden");
  } else {
    document.getElementById("login").removeAttribute("hidden");
    document.getElementById("register").removeAttribute("hidden");
  }
}

