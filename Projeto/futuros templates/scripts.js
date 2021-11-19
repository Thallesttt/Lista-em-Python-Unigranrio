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