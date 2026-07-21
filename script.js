let searchInput = document.getElementById("searchInput")
let searchBtn1 = document.getElementById("searchBtn")
let postinput = document.getElementById("postinput")
let postBtn = document.getElementById("post")
let allposts = document.getElementById("allposts")




postBtn.addEventListener("click",function(){
    let postText = postinput.value;                    // this will whatever text type by user { post.text will make that text in variable}
    if(postText == ""){
        return;                                       // this will not post any thing if input is emapt
    }
    let newPost = document.createElement("p");
    newPost.innerText = postText;                     // puts the user text inside the <p>
    let deleteBtn = document.createElement("button")  // we have created new button "delete"
    deleteBtn.innerText = "Delete"                    // the "delete" word is shown on deleteBtn button
    deleteBtn.addEventListener("click",function(){
        newPost.remove();                             // this will remove new post 
        deleteBtn.remove();                          // this will remove delete button
    });
    allposts.appendChild(newPost)                     // add the <p> to the web page
    allposts.appendChild(deleteBtn)                   // button will come below the new post
    postinput.value = "";                             // clear the input after posting
    console.log(postText);                             // this is display that text in console
});

