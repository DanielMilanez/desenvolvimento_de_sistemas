const frm = document.querySelector("form");
const resp = document.getElementById("resposta");

function mostrarFrutas(){
    const number = Number(frm.vezesRepetir.value);
    
    for(let i = 0; i <= number; i++){
        const nameFruta = frm.nameFruta.value;
        resp.innerText += `${nameFruta} * `;
    }
}   