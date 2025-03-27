const frm = document.querySelector("form");
const h3 = document.querySelector("h3");
const h4 = document.querySelector("h4");

frm.addEventListener("submit", (e)=>{
    const nome = frm.inNome.value;
    const nota = Number(frm.inNota.value);
    const nota2 = Number(frm.inNota2.value);

    const media = (nota + nota2) / 2;

    if(media > 7){
        h3.innerText = `O ${nome} foi aprovado.`
        h4.innerText = `A média é: ${media.toFixed(2)}`
    }
    else{
        h3.innerText = `O ${nome} foi reprovado.`
        h4.innerText = `A média é: ${media.toFixed(2)}`
    }
    e.preventDefault();
});