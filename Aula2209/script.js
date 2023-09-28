function consultaCep() {
    var $cep = document.getElementsById("cep").value.replace(/\D/g, '');
    var url = 'https://viacep.com.br/ws' + $cep + '/json/';
    var request = new XMLHttpRequest();

    request.open('GET', url);
    request.onerror = function(e) {
        document.getElementsById('return').innerHTML = 'invalido'
    }
request.unload = () => {
    var response = JSON.parse(request.responseText);

    if (response.erro === true) {
document.getElementsById('return').innerHTML = 'CEP nao encontrado';
    }else{
        document.getElementById('return').innerHTML = 'CEP: ' + response.cep +'<br>' +
                                                      'Logadouro: ' + response.logadouro +'<br>' +
                                                      'Bairro: ' + response.bairro + '<br>' +
                                                      'Cidade: ' + response.localidade;
    }
}
request.send();
}
