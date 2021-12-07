function getFormData(form_id) {
    return Array.from(document.querySelectorAll(`#${form_id} input`)).reduce((acc, input) => ({ ...acc, [input.id]: input.value}),{});
}

function setCookie(cname, cvalue, exdays=1) {
  const d = new Date();
  d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
  let expires = "expires="+d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function deleteCookie(cname) {
  setCookie(cname, '', -1)
}

function getCookie(cname) {
  let name = cname + "=";
  let ca = document.cookie.split(';');
  for(let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

function checkCookie() {
  let user = getCookie("username");
  if (user != "") {
    alert("Welcome again " + user);
  } else {
    user = prompt("Please enter your name:", "");
    if (user != "" && user != null) {
      setCookie("username", user, 365);
    }
  }
}

function login(username, password){
    console.log(`Username ${username}`)
    console.log(`Password ${password}`)
    fetch("/api/login/", {
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "username": username,
            "password": password
        }),
        method: "POST"
    })
    .then(response=>response.json())
    .then(result=>{
        if("token" in result){
            setCookie("token", result["token"])
            location.replace("/")
        }
        else{
            alert("User or password incorrect")
        }
    })
}

function user_is_logged_in(){
    if(getCookie("token") != undefined && getCookie("token") != ''){
        return true
    }
    else{
        return false
    }
}

function logout(){
    deleteCookie("token")
    location.replace("/")
}