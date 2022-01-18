function httpPostAsync(method, params, callback) {

    var xmlHttp = new XMLHttpRequest();

    xmlHttp.onreadystatechange = function() {

    if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
        callback(xmlHttp.responseText);
    else
        callback('Ожидание ответа ...');
    }

    xmlHttp.open("POST",  method, true);
    xmlHttp.setRequestHeader("Content-Type", "application/json");
    xmlHttp.send(params);
}

function getShortLink(){
    var longlink = document.getElementById("longlink").value;
    httpPostAsync("getShortLink", JSON.stringify({ "data": longlink }), function(resp){
        response = `${resp}`;
        document.getElementById("shortlink").textContent = response;
    });

}