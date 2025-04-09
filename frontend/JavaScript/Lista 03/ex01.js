const frm = document.querySelector("form");
const resp = document.querySelector("h3");

frm.addEventListener("submit", (e)=>{
    e.preventDefault();
    const nome = frm.inName.value;
    const mascluno = frm.inMasculino.checked;
    const altura = Number(frm.inAltura.value);

    // Operador ternário em JS
    let peso = mascluno ? Math.pow(altura, 2) * 22 : Math.pow(altura, 2) * 21;

    resp.innerText = `${nome}: Seu peso ideal é ${peso.toFixed(2)}kg`;
});

function limpar(){
    document.querySelector("h3").innerText = "";
}
