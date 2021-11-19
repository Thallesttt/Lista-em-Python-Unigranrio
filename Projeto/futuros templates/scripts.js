function submitType(Elemento_HTML) {

    var classtype = Elemento_HTML.classList;

    switch (classtype.value) {
        case "POST":
            Elemento_HTML.method = "POST";
            let obj = {};
            for (var objparam of Elemento_HTML.elements) {
                paramname = objparam.id;
                paramvalue = objparam.value;
                Object.defineProperty(obj, `${paramname}`, { value: paramvalue });

            }
            return obj;


        case "GET":
            Elemento_HTML.method = "GET";
            let strObj = "?";
            for (var param of Elemento_HTML.elements) {
                strObj = strObj.concat(`${param.id}=${param.value}&&`);
            }
            strObj = strObj.substr(0, strObj.length - 2)
            return strObj;
    }

}

async function check_length(string, check = false) {

    if (string.length >= 6) { check = true; }
    return check;
}

async function check_variety(string, num = 0, check = false) {
    array = ["%", "&", "!", "@", "#", "$", "_", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
    for (let letter of string) {
        if (array.find(p => { return p == letter })) {
            array.splice(array.findIndex(p => { return p == letter }), 1);
            num++;
        }

        if (num >= 6) { check = true; }
    }
    return check;
}

async function check_database(string, url = "http://127.0.0.1:8000/Usuario.json") {
    let obj = "";
    let xhr = new XMLHttpRequest();
    xhr.open("GET", url, true);
    xhr.responseType = "text";
    xhr.onreadystatechange = () => {

        switch (xhr.readyState) {
            case 4: obj = xhr.responseText;
                obj = JSON.parse(obj);
                for (var usuario of obj) {
                    if (string == usuario.senha) {
                        console.log("senha já existe no banco");
                    }
                }
                break;
        }

    }
    xhr.send();
}