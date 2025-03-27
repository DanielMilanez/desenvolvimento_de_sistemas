const frm = document.querySelector("form");

frm.addEventListener("submit", (e)=>{
    e.preventDefault();

    const id = frm.inID.value;
    if(id != ""){
        atualizar(id);
    }else{
        incluir();
    }
});

let lista = [];
const tbody = document.querySelector("tbody");

function incluir(){
    lista.push(frm.inItem.value);
    atualizarPagina();
}

function atualizarPagina(){
    tbody.innerHTML = "";

    for(let i in lista){
        tbody.innerHTML += `<tr><td onclick="editar(${i})"> ${lista[i]}</td></tr>`;
    }
    frm.reset() // deixando o formulario no original
}

function editar(i){
    frm.inItem.value = lista[i];
    frm.inID.value = i;
}

function apagar(){
    if(frm.inID.value != ""){
        lista.splice(frm.inID.value,1); // informando a partir de qual e de quantos, no caso 1
        atualizarPagina(); // chamar a atualização de lista
    }else{
        alert("Clique no item que você deseja apagar");
    }
}

function atualizar(i){
    lista[i] = frm.inItem.value;
    atualizarPagina();
}
