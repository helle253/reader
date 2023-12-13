let host = "http://localhost:5000"

document.getElementById("register").addEventListener("click", register);
document.getElementById('password').addEventListener('change', check);
document.getElementById('confirm_password').addEventListener('change', check);

function check() {
  console.log('checking1');
  if (document.getElementById('password').value ==
    document.getElementById('confirm_password').value) {
    document.getElementById('message').style.color = 'green';
    document.getElementById('message').innerHTML = 'matching';
    console.log('matching')
  } else {
    document.getElementById('message').style.color = 'red';
    document.getElementById('message').innerHTML = 'not matching';
    console.log('not matching')
  }
}

async function register(){
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