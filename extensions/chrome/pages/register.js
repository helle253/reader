import host from '../common/host.js';

document.getElementById("register").addEventListener("click", register);
document.getElementById('password').addEventListener('change', check);
document.getElementById('confirm_password').addEventListener('change', check);

function check() {
  if (document.getElementById('password').value ==
    document.getElementById('confirm_password').value) {
    document.getElementById('message').style.color = 'green';
    document.getElementById('message').innerHTML = 'matching';
    return true;
  } else {
    document.getElementById('message').style.color = 'red';
    document.getElementById('message').innerHTML = 'not matching';
    return false;
  }
}

async function register(){
  if (!check()) return;

  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  const resp = await fetch(host + "/auth/register", {
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
  window.location.href = "index.html";
}
