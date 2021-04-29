const form = document.querySelector(".signup form"),
continueBtn = form.querySelector(".button input");

form.onsubmit = (e)=> {
    e.preventDefault();// prevent form from submitting.
}

continueBtn.onclick = ()=> {
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "assets/python/login.py", true);
    xhr.onload = ()=> {
        if(xhr.readyState == XMLHttpRequest.DONE){
            if(xhr.status == 200){
                let data = xhr.response;
                console.log(data);
            }
        }
    }
}
