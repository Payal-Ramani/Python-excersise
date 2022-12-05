let arr = [{
    name: "Payal",
    email: "payalramani4@gamil.com",
    gender: "Female",
    hobby: ["Reading", "Sports"],
    age : 23,
    country : "India",
    state: "Gujarat",
    city: "Surat",
    time : new Date()
},
{
    name: "Jemika",
    email: "jh4@gamil.com",
    gender: "Female",
    hobby: ["Reading", "Travelling"],
    age : 22,
    country : "India",
    state: "Gujarat",
    city: "Gandhinagar",
    time : new Date()
}]

function displayData(search) {
    let td = document.getElementById('tabledata');
    td.innerHTML = "";
    let newdata = "";
    if(!search){

        let len = arr.length;
        for (let i = 0; i < len; i++) {
            newdata += '<tr>';
            newdata += '<td>' + arr[i].name + '</td>' + '<td>' + arr[i].email + '</td>' + '<td>' + arr[i].gender + '</td>' + '<td>' + arr[i].hobby + '</td>'+'<td>'+arr[i].age + '</td>' +'<td>'+ arr[i].country + '</td>' + '<td>' + arr[i].state + '</td>' + '<td>' + arr[i].city + '</td>' +'<td>'+timing(arr[i].time) +'</td>' + '<td>' + `<a onclick="deleteData(${i})"><i class="fa-solid fa-trash"></i> </a>` + '</td>' + '<td>' + `<a onclick="updateForm(${i})"><i class="fa-solid fa-pen-to-square"></i></a>` + '</td>';
            newdata += '</tr>'
        };
        td.innerHTML += newdata;
    }
    else{
        let len1 = search.length
        if(len1 == 0){
            newdata += `<td> No data found...</td>`
        }
        else{
            for(let i = 0;i < len1;i++){
                newdata += '<tr>';
                newdata += '<td>' + search[i].name + '</td>' + '<td>' + search[i].email + '</td>' + '<td>' + search[i].gender + '</td>' + '<td>' + search[i].hobby + '</td>'+'<td>'+search[i].age + '</td>' +'<td>'+ search[i].country + '</td>' + '<td>' + search[i].state + '</td>' + '<td>' + search[i].city + '</td>' +'<td>'+timing(search[i].time) +'</td>' + '<td>' + `<a onclick="deleteData(${i})"><i class="fa-solid fa-trash"></i> </a>` + '</td>' + '<td>' + `<a onclick="updateForm(${i})"><i class="fa-solid fa-pen-to-square"></i></a>` + '</td>';
                newdata += '</tr>'
            }
        }
        td.innerHTML += newdata;

    }

    let getcon = document.getElementById('country');
    getcon.innerHTML = "";
    getcon.innerHTML = `<option value=""> Select Country </option> `;
        for (let x in address) {

            let opt = document.createElement('option');
            opt.text = x;
            opt.value = x;
            getcon.appendChild(opt);
        }
};

function timing(t){
    let date = t.getDate();
    let month = t.getMonth();
    let year = t.getFullYear();
    let hour = t.getHours();
    let minute = t.getMinutes();
    let sec = t.getSeconds();
    return `${date}/${month}/${year}  ${hour}:${minute}:${sec}`

};

