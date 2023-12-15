import host from '../scripts/common/host.js';
import tokenPairFromCookie from '../scripts/common/tokenPairFromCookie.js'

document.addEventListener("DOMContentLoaded", loadState);

document.getElementById('logout').addEventListener('click', logout);

var tokenPair;

async function loadState() {
  tokenPair = await tokenPairFromCookie();

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
