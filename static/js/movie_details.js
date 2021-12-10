function print_review(review){
    div_card = document.createElement("div")
    div_card.className = "card h-100"

    div_body = document.createElement("div")
    div_body.className = "card-body"
    div_card.appendChild(div_body)

    title = document.createElement("p")
    title.className = "card-title"
    title.innerText = review.title
    div_body.appendChild(title)

    comment = document.createElement("p")
    comment.className = "card-text"
    comment.innerText = review.comment
    div_body.appendChild(comment)

    stars = document.createElement("p")
    stars.className = "card-text"
    stars.innerText = "Stars: "
    div_body.appendChild(stars)

    stars_value = document.createElement("span")
    stars_value.innerText = review.stars
    stars.appendChild(stars_value)

    username = document.createElement("p")
    username.className = "card-text"
    username.innerText = "User: "
    div_body.appendChild(username)

    username_value = document.createElement("span")
    username_value.innerText = review.user.username
    username.appendChild(username_value)

    published_date = document.createElement("p")
    published_date.className = "card-text"
    published_date.innerText = "Published Date: "
    div_body.appendChild(published_date)

    let date = new Date(review.published_date);
    let day = `0${date.getDate()}`.slice(-2); //("0"+date.getDate()).slice(-2);
    let month = `0${date.getMonth() + 1}`.slice(-2);
    let year = date.getFullYear();
    published_date_value = document.createElement("span")
    published_date_value.innerText = `${day}-${month}-${year}`
    published_date.appendChild(published_date_value)

    return div_card
}

function print_reviews(reviews){
    var parent_div = document.getElementById("list_reviews_div")

    reviews.forEach(function(review){
        var div = document.createElement("div")
        div.className = "mt-1"
        div.appendChild(print_review(review))
        parent_div.appendChild(div)
    })
}

function print_movie_details(id){
    get_movie(id)
    .then(result=>{

        if(result.detail == "Not found."){
            location.replace("/")
        }

        image = document.getElementById("image")
        image.src = result["image"]
        image.height = 500

        title = document.getElementById("title")
        title.innerText = result["title"]


        category = document.getElementById("category")
        category.innerText = result["category"].title


        synopsis = document.getElementById("synopsis")
        synopsis.innerText = result["synopsis"]

        print_reviews(result["reviews"])

    })
}

function check_user(){
    if(!user_is_logged_in()){
        form = document.getElementById("create_review_form")
        form.style.display = "none"

        parent = form.parentElement

        p = document.createElement("p")
        p.innerText = "Login to create a review"
        parent.appendChild(p)

        a = document.createElement("a")
        a.className = "btn btn-primary"
        a.href = "/login/"
        a.innerText = "Login"
        parent.appendChild(a)


    }
}

function clear_form(form_id){
    form = document.getElementById(form_id)
    form.reset()
}

function clear_reviews(){
    const parent_div = document.getElementById("list_reviews_div");
    while (parent_div.firstChild) {
        parent_div.removeChild(parent_div.lastChild);
    }
}

function create_review(movie_id){
    if(!user_is_logged_in()){
        alert("User is not logged in")
        return
    }

    token = getCookie("token")
    form_data = getFormData("create_review_form")
    fetch("/api/reviews/", {
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Token ${token}`
        },
        method: "POST",
        body: JSON.stringify({
                "title": form_data["review_title"],
                "comment": form_data["comment"],
                "stars": form_data["stars"],
                "movie": movie_id
        })
    })
    .then(response=>response.json())
    .then(result=>{
        clear_form("create_review_form")
        print_reviews([result])
    })
}