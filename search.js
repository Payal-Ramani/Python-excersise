

function findData() {
    let entry = document.getElementById('find').value
    if(entry !== ""){
        let serarr = arr.filter(arra=>{
            if( arra.name.toLowerCase().indexOf(entry.toLowerCase()) > -1 )
            return arra;
        })
        displayData(serarr);
    }
}



