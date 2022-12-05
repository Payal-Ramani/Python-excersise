const ascData = () => {
    arr.sort((a, b) => {
        let fa = a.name.toLowerCase(),
            fb = b.name.toLowerCase();
        if (fa < fb) {
            return -1;
        }
        else if (fa > fb) {
            return 1;
        }
        return 0;
    });
    displayData(arr);
}

const desData = () => {
    arr.sort((a, b) => {
        let fa = a.name.toLowerCase(),
            fb = b.name.toLowerCase();
        if (fa > fb) {
            return -1;
        }
        else if (fa < fb) {
            return 1;
        }
        return 0;
    });
    displayData(arr);
}

function dataSorting() {
    let val = document.getElementById('sorting');
    if (val.value == "Ascending") {
        ascData();
    }
    if (val.value == "Descending") {
        desData();
    }
}
