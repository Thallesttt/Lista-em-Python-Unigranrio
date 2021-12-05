
async function password_safety(string, checkCount = 0) {
    try {
        if (await check_length(string)) { checkCount++; }
        if (await check_variety(string)) { checkCount++; }
        var refSenha = document.getElementById("Senha");

        if (string === refSenha.value) { checkCount++; }

        // checkCount = await check_length(string) == true ? checkCount++ : checkcount;
        // checkCount = await check_variety(string) == true ? checkCount++ : checkcount;
        // checkCount = string === refSenha.value ? checkCount++ : checkCount;

        if (checkCount < 3) {
            throw new Error("Senha não obteve todos os requisitos para ser aceita");
        }
        console.log(checkCount);

        if (await check_database(string)) { throw new Error("Senha já existe no Banco"); };
        console.log("Senha Aceita");
    }
    catch (erro) { console.log(erro.message); }

}

function submit() {
    obj = { Nome: "", Senha: "", Cep: "", Estado: "", Endereco: "", Bairro: "" };
    var registration = document.getElementById("formcadastro");
    for (var x = 1; x < registration.length; x++) {
        obj.Nome = registration[x].value; x++;
        obj.Senha = registration[x].value; x++;
        obj.Cep = registration[x].value; x++;
        obj.Endereco = registration[x].value; x++;
        obj.Bairro = registration[x].value; x++;
        obj.Estado = registration[x].value; x++;
    }
    var xhr = new XMLHttpRequest();
    xhr.open("GET", `http://127.0.0.1:8000/Usuario.json`, true);
    xhr.responseType = "text";
    xhr.onreadystatechange = () => {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var array_obj = JSON.parse(xhr.response);
            array_obj.push(obj);
            arrray_obj = JSON.stringify(array_obj);
            console.log(array_obj);
        }
    }
    xhr.send();
}

async function pesquisaEndereco(string) {
    var string = string.replace("-", "");
    var formatado = string.replace(/^(\d{5})(\d{3})*/, '$1-$2');
    cep.value = formatado;
    url = `https://viacep.com.br/ws/${string}/json/`;
    var http = new XMLHttpRequest();
    http.open("GET", url, true, "0");
    http.onreadystatechange = () => {

        if (http.readyState == 4 && http.status == 200) {
            // console.log(http.responseText);
            var objEndereco = JSON.parse(http.responseText);
            document.getElementById("Endereco").value = objEndereco.logradouro;
            document.getElementById("Bairro").value = objEndereco.bairro;
            document.getElementById("Estado").value = objEndereco.uf;
        }
    };
    http.send();

}

var senha = document.getElementById("Senha");
senha.addEventListener("keyup", async function () {
    var x = document.getElementById("teste_senha");
    switch (this.value.length) {
        case (1 || 2 || 3 || 4 || 5): x.style.backgroundColor = "#ff0b03";
            break;
        case (6 || 7 || 8):
            x.style.backgroundColor = "#f9ea00";
            break;
    }
    if (this.value.length > 8) {
        x.style.backgroundColor = "#4cff0e";
    }
})
senha.addEventListener("focusout", async function () {
    return await password_safety(this.value);
});

var cep = document.getElementById("Cep");

cep.addEventListener("change", async function () { await pesquisaEndereco(this.value) });

console.log("Teste");