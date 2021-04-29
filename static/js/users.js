const searchBar = document.querySelector(".userList .search input"),
searchBtn = document.querySelector(".userList .search button");

searchBtn.onclick = ()=>{
    searchBar.classList.toggle("active");
    searchBar.focus();
    searchBtn.classList.toggle("active");
}

