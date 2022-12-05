function validateData() {
    let name = document.getElementById('name');
    let email = document.getElementById('Email');
    let genmale = document.getElementById('Male');
    let genfemale = document.getElementById('Female');
    let hobby1 = document.getElementsByName('hobby');
    let hobby = [];
    for (let i = 0; i < hobby1.length; i++) {
        if (hobby1[i].checked)
            hobby.push(hobby1[i].value);
    }
    let age = document.getElementById('age');
    let country = document.getElementById('country');
    let state = document.getElementById('state');
    let city = document.getElementById('city');


    function validateForm(tagName,str){
        let newnode = document.createElement('p');
        newnode.classList = "paragraph";
        newnode.id = `${str}-error`;
        newnode.innerHTML = `Please enter your ${str}.`;
        let parentDiv = tagName.parentNode;
        parentDiv.insertBefore(newnode,tagName);
    }
    if (name.value == "") {
        if (!document.getElementById('name-error')) {
            validateForm(name,'name');
            
        }
    } else {
        if (document.getElementById('name-error')) {
            document.getElementById('name-error').remove();
        }
    }

    if (email.value == "") {
        if (!document.getElementById('email-error')) {
            validateForm(email,'email')
            
        }
    } else {
        if (document.getElementById('email-error')) {
            document.getElementById('email-error').remove();
        }
    }

    if (genmale.checked == false && genfemale.checked == false) {
        if (!document.getElementById('gender-error')) {
            validateForm(genmale,'gender')
            
        }
    }else {
        if (document.getElementById('gender-error')) {
            document.getElementById('gender-error').remove();
        }
    }

    if (hobby.length == 0) {
        if (!document.getElementById('hobby-error')) {

            let hobbypara = document.createElement('p');
            hobbypara.classList = "paragraph";
            hobbypara.id = 'hobby-error';
            hobbypara.innerHTML = "Please select atleast one from these hobbies."
            let parentDiv4 = document.getElementById('reading').parentNode;
            parentDiv4.insertBefore(hobbypara, document.getElementById('reading'))
        }
    }else {
        if (document.getElementById('hobby-error')) {
            document.getElementById('hobby-error').remove();
        }
    }

    if (age.value == "") {
        if (!document.getElementById('age-error')) {
            validateForm(age,'age');
        }
    }else {
        if (document.getElementById('age-error')) {
            document.getElementById('age-error').remove();
        }
    }

    if (country.value == "") {
        if (!document.getElementById('country-error')) {
            validateForm(country,'country')
        }
    }else {
        if (document.getElementById('country-error')) {
            document.getElementById('country-error').remove();
        }
    }

    if (state.value == "") {
        if (!document.getElementById('state-error')) {
            validateForm(state,'state')
        }
    }else {
        if (document.getElementById('state-error')) {
            document.getElementById('state-error').remove();
        }
    }

    if (city.value == "") {
        if (!document.getElementById('city-error')) {
            validateForm(city,'city')
        }
    }else {
        if (document.getElementById('city-error')) {
            document.getElementById('city-error').remove();
        }
    }


}
