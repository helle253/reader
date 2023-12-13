document.addEventListener("DOMContentLoaded", loadState);

document.getElementById('logout').addEventListener('click', logout);

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

  updateUI(!!tokenPair)
}

function updateUI(isLoggedIn) {
  if (isLoggedIn) {
    document.getElementById("login").setAttribute("hidden", '');
    document.getElementById("register").setAttribute("hidden", '');
    document.getElementById("logout").removeAttribute("hidden");
  } else {
    document.getElementById("logout").setAttribute("hidden", '');
    document.getElementById("login").removeAttribute("hidden");
    document.getElementById("register").removeAttribute("hidden");
  }
}

function logout() {
  chrome.cookies.remove({url: host, name: "tokenPair"})
  updateUI(false)
}
