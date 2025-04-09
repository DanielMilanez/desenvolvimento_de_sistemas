const frm = document.querySelector("form");

function verificaNumero(){
    const number = Number(frm.inNumber.value);

    for(let i = 0; i < number; i ++){
        if (number % i == 0){
            // Parei aqui
        }
    }

}
