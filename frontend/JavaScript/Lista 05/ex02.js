const frm = document.querySelector("form");
const resp = document.getElementById("response")

function preverChinchila(){
    const num = Number(frm.numChinchilas.value);
    const anos = Number(frm.quantidadeAnos.value);
    let total = 0;

    for(let i = 1; i <= anos; i++){
        
        if(total == 0){
            total += num; 
        }
        else{
            total *= 3;
        }

        resp.innerText += (`${i}° ano: ${total} chinchilas \n`);
    }
}
