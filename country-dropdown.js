

function selectState(val) {
    let getstat = document.getElementById('state');
    getstat.innerHTML = "";
    getstat.innerHTML = `<option value=""> Select State </option>`;
    for (let x in address[val]) {
        let opt = document.createElement('option');
        opt.value = x;
        opt.text = x;
        getstat.appendChild(opt);
    }
    selectCity("");
}

function selectCity(val) {
    let getcit = document.getElementById('city');
    if (val == "") {
        getcit.innerHTML = "";
        getcit.innerHTML = `<option value=""> Select City </option>`;

    }
    else {
        let count = document.getElementById('country').value;
        getcit.innerHTML = "";
        getcit.innerHTML = `<option value=""> Select City </option>`;
        address[count][val].forEach(element => {
            let opt = document.createElement('option');
            opt.value = element;
            opt.text = element;
            getcit.appendChild(opt);
        });
    }
}