function submitData(){
    event.preventDefault();
    let name = document.getElementById('name').value;
    let email = document.getElementById('Email').value;
    let gender = document.querySelector('input[name = "Gender"]:checked').value;
    let hobby = document.getElementsByName('hobby');
    let arrOfHobby = [];
    for(let i = 0;i<hobby.length;i++){
        if(hobby[i].checked )
            arrOfHobby.push(hobby[i].value);
    }
    let age = document.getElementById('age').value;
    let country = document.getElementById('country').value;
    let state = document.getElementById('state').value;
    let city = document.getElementById('city').value;
    let time = new Date();

    if(name && email && gender && hobby.length != 0 && age && country && state && city){

        arr.push({
            name : name,email : email ,gender: gender,hobby : arrOfHobby,age : age,country : country ,state : state ,city:city ,time : time
        });
    
        displayData("");
        document.getElementById('main-form').reset();
    }
}