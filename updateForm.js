function updateForm(index){

    document.getElementById('main-form').reset();
    document.getElementById('name').value = arr[index].name;
    document.getElementById('Email').value = arr[index].email;
    if(arr[index].gender == "Male"){
        document.getElementById('Male').checked = true;
    }else if(arr[index].gender == "Female"){
        document.getElementById('Female').checked = true;
    }
   
    if(arr[index].hobby.includes("Reading") == true){
        document.getElementById('reading').checked = true;
    }
     if(arr[index].hobby.includes("Travelling")== true){
        document.getElementById('travelling').checked = true;
    }
     if(arr[index].hobby.includes("Sports")== true){
        document.getElementById('sports').checked = true;
    }

    document.getElementById('age').value = arr[index].age;
    document.getElementById('country').value = arr[index].country;
  
    selectState(arr[index].country);
    document.getElementById('state').value = arr[index].state;
    selectCity(arr[index].state);
    document.getElementById('city').value = arr[index].city;
    
    
    let butSub = document.getElementById('forcreatebtn');
    butSub.innerHTML = "";
    
    but = document.createElement('button');
    // but.value = "cancel";
    but.innerHTML = "Cancel";
    // but.id = "cancel";
    but.addEventListener('click',cancelData);
    butSub.appendChild(but);
  

    upd = document.createElement('button');
    // upd.value = "update";
    upd.innerHTML = "Update";
    // upd.id = "update";
    upd.addEventListener("click",updateData)
    butSub.appendChild(upd);

    // document.getElementById('cancel').addEventListener("click",cancelData);
    function cancelData(){
        
        document.getElementById('main-form').reset();
        // document.getElementById('cancel').style.display = "none";
        // document.getElementById('update').style.display = "none";
        butSub.innerHTML = ""
        sub = document.createElement('button');
        // sub.value = "submit";
        sub.innerHTML = "Submit";
        sub.addEventListener('click',submitData);
        butSub.appendChild(sub);
        event.preventDefault();
    }

    function updateData(){
        arr[index].name = document.getElementById('name').value;
        arr[index].email = document.getElementById('Email').value;
        arr[index].gender = document.querySelector('input[name="Gender"]:checked').value;
        let hobby = document.getElementsByName('hobby');
        let hobbyArray = [];
        for(let i = 0; i < hobby.length;i++){
            if(hobby[i].checked == true){
                hobbyArray.push(hobby[i].value)
            }
        }
        arr[index].hobby = hobbyArray;
        arr[index].age = document.getElementById('age').value;
        arr[index].country = document.getElementById('country').value;
        arr[index].state = document.getElementById('state').value;
        arr[index].city = document.getElementById('city').value;
    
        displayData("");
        cancelData();
        // clearData();
        // event.preventDefault();
    
        // function clearData(){
        //     document.getElementById('update').style.display = 'none';
        //     document.getElementById('cancel').style.display = 'none';
        //     // document.getElementById('submit').style.display = 'block';
        //     // document.getElementById('main-form').reset();
        //     event.preventDefault();
        // }
        // // event.preventDefault();
    }
}
   

function deleteData(index){
    arr.splice(index,1);
    displayData("");
}
