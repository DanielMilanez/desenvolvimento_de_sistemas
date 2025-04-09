const frm = document.querySelector("form");
const response = document.querySelector("h3");
const responseTroco = document.querySelector("h4");

function calcular(){
    const value = Number(frm.inValor.value);
    var troco = 0;

    if (value < 1){
        response.innerText = "Valor inválido!";
    }
    else if(value < 1.75){
        response.innerText = "Tempo: 30";
        troco = value - 1;
    }
    else if(value < 3){
        response.innerText = "Tempo: 60";
        troco = value - 1.75;
    }
    else if(value >= 3){
        response.innerText = "120";
        troco = value - 3;
    }
    responseTroco.innerText = `Valor total do troco: R$${troco.toFixed(2)}`;
}
