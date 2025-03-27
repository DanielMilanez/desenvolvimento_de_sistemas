function execute02() {
    const ValorConta = Number(prompt("Informe o valor da conta: "));
    const NumClientes = Number(prompt("Informe a quantidade de clientes para dividir a conta: "));

    alert(`O valor pago por cliente será de: R$${(ValorConta / NumClientes).toFixed(2)}`);
}