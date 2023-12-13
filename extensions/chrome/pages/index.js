document.addEventListener("DOMContentLoaded", loadState);

document.getElementById("clickMe").addEventListener("click", myFunction);
document.getElementById("login").addEventListener("click", login);

let host = "http://localhost:5000"
var tokenPair;

async function loadState() {
  const cookie = await chrome.cookies.get({url: host, name: "tokenPair"});
  tokenPair = JSON.parse(cookie.value || '{}');
}

function myFunction(){
  console.log('clicked!');
}

async function login(email, password){
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
  tokenPair = (await resp.json())["data"]
  chrome.cookies.set({url: host, name: "tokenPair", value: JSON.stringify(tokenPair)})
}
