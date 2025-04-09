const frm = document.querySelector("form");
const response = document.querySelector("h3");
const canvas = document.getElementById("trianguloCanvas");
const ctx = canvas.getContext("2d");

function verificaTriangulo() {
    const ladoA = Number(frm.ladoA.value);
    const ladoB = Number(frm.ladoB.value);
    const ladoC = Number(frm.ladoC.value);

    let verifica = ladoA + ladoB > ladoC && ladoB + ladoC > ladoA && ladoA + ladoC > ladoB;

    if (verifica) {
        if (ladoA === ladoB && ladoB === ladoC) {
            response.innerText = `Podem formar um triângulo Equilátero`;
        } else if (ladoA !== ladoB && ladoB !== ladoC && ladoA !== ladoC) {
            response.innerText = `Podem formar um triângulo Escaleno`;
        } else {
            response.innerText = `Podem formar um triângulo Isósceles`;
        }
        desenhaTriangulo(ladoA, ladoB, ladoC);
    } else {
        response.innerText = `Valores inseridos não podem formar um triângulo`;
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    }
}

function desenhaTriangulo(ladoA, ladoB, ladoC) {
    const scale = 10; // Fator de escala para aumentar o triângulo

    // Limpa o canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Define as cores
    const cores = ["red", "green", "blue"];

    // Calcula as coordenadas dos vértices do triângulo
    const altura = (ladoA * Math.sqrt(3)) / 2; // Altura baseada em ladoA
    const x1 = canvas.width / 2; // Vértice 1 (cima)
    const y1 = 50; // Vértice 1 (altura)
    const x2 = x1 - (ladoB * scale) / 2; // Vértice 2 (esquerda)
    const y2 = y1 + altura * scale; // Vértice 2 (base)
    const x3 = x1 + (ladoB * scale) / 2; // Vértice 3 (direita)
    const y3 = y2; // Vértice 3 (base)

    // Desenha o triângulo
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.lineTo(x3, y2);
    ctx.closePath();
    ctx.fillStyle = "rgba(0, 0, 0, 0.4)"; // Cor de preenchimento
    ctx.fill();
    ctx.stroke();

    // Desenha os lados com cores diferentes
    ctx.lineWidth = 5;

    ctx.strokeStyle = cores[0]; // Vermelho
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();

    ctx.strokeStyle = cores[1]; // Verde
    ctx.beginPath();
    ctx.moveTo(x2, y2);
    ctx.lineTo(x3, y2);
    ctx.stroke();

    ctx.strokeStyle = cores[2]; // Azul
    ctx.beginPath();
    ctx.moveTo(x3, y2);
    ctx.lineTo(x1, y1);
    ctx.stroke();

    // Adiciona os valores dos lados nos respectivos lados
    ctx.fillStyle = "#000"; // Cor do texto
    ctx.font = "16px Arial";
    
    // Texto no lado A (acima do vértice superior)
    ctx.fillText(`Lado A: ${ladoA}`, x1 - 20, y1 - 10);
    // Texto no lado B (abaixo do lado esquerdo)
    ctx.fillText(`Lado B: ${ladoB}`, x2 - 40, y2 + 20);
    // Texto no lado C (abaixo do lado direito)
    ctx.fillText(`Lado C: ${ladoC}`, x3 + 10, y2 + 20);

    // Exibe o canvas
    canvas.style.display = "block";
}
