function execute04() {
    const valueDinner = Number(prompt("Insira o valor do jantar: "));
    const taxWaiter = 0.10 * valueDinner;

    const valorTotal = valueDinner + taxWaiter;
    alert(`O valor total ${valorTotal.toFixed(2)} \n o valor da taixa de comissão é ${taxWaiter.toFixed(2)} \n o valor total a pagar é: ${valorTotal.toFixed(2)}`);
}
