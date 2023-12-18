import host from '../scripts/common/host.js';

document.getElementById("login").addEventListener("click", login);

async function login(){
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  const resp = await fetch(host + "/auth/login", {
    method: "POST",
    body: JSON.stringify({
      email: email,
      password: password,
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8"
    }
  });
  const tokenPair = (await resp.json())["data"]
  const sevenDaysMs = 1000 * 60 * 60 * 24 * 7
  chrome.cookies.set({
    expirationDate: Date.now() + sevenDaysMs,
    url: host,
    name: "tokenPair",
    value: JSON.stringify(tokenPair),
    })
  window.location.href = "index.html";
}
