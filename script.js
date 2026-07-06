let post = document.getElementById("post");       // we are calling post id
let postinput = document.getElementById("postinput");  // we are calling postinput id
let newpost = document.getElementById("newpost") ;     // we are calling new post id
let allposts = document.getElementById("allposts");

post.addEventListener("click",function(){
    if (postinput.value == ""){
        return;
    }
    allposts.innerHTML += "<p>" + postinput.value + "</p>";     // add new post inside allpost
    postinput.value = "" ;           // clear input box after posting
});