const frm = document.querySelector("form");
const resp = document.querySelector("h3");
const resp2 = document.querySelector("h4");

frm.addEventListener("submit", (e)=>{
    const medicamento = frm.inMed.value;
    const price = frm.inPrice.value;

    resp.innerText = `Promoção de ${medicamento}`;
    resp2.innerText = `Leve 2 únidades por R$${(Math.floor(price) * 2).toFixed(2)}`;

    e.preventDefault()
});
