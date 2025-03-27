function execute03() {
    // Exibindo números pares.
    const num = Number(prompt("Informe o número: ")); 

    if (num % 2 == 0){
        alert(`O número ${num} é par!`);
    }
    else{
        alert(`O número ${num} é impar!`);
    }
}