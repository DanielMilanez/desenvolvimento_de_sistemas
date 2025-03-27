function execute03() {
    const Price = Number(prompt("Digite o preço do produto: R$"));

    alert(`O pagamento à vista será de: R$ ${Price - Price * 0.1}`);
    alert(`O pagamento dividido em 3x COM JUROS é R$ ${((Price  + Price * 0.1) / 3).toFixed(2)}`);
}