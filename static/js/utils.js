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


function get_movies(filters){
    return fetch("/api/movies/", {
        headers: {
            "Content-Type": "application/json"
        },
        method: "GET"
    })
    .then(response=>response.json())
    .then(result=>{
        return result
    })
}

function print_movie(movie){
    var div1 = document.createElement("div")
    div1.className ="card h-100"

    var img = document.createElement("img")
    img.src = movie.image
    img.alt = "movie image"
    img.height = 300
    div1.appendChild(img)

    var div2 = document.createElement("div")
    div2.className = "card-body"
    div1.appendChild(div2)

    var h5 = document.createElement("h5")
    h5.className = "card-title"
    h5.innerText = movie.title
    div1.appendChild(h5)

    if(movie.category != null){
        var p = document.createElement("p")
        p.className = "card-text"
        p.innerText = movie.category.title
        div1.appendChild(p)
    }

    var a = document.createElement("a")
    a.className = "btn btn-primary"
    a.href = "#"
    a.innerText = "Details"
    div1.appendChild(a)

    return div1
}

function print_movies(movies){
    var parent_div = document.getElementById("list_movies_div")
    movies.forEach(function(movie){
        var div = document.createElement("div")
        div.className = "col-3 mt-5"
        div.appendChild(print_movie(movie))
        parent_div.appendChild(div)
    })
}