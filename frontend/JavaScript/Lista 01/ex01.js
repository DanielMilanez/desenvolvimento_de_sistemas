function execute01() {
    // Elaborar um programa que leia um número. Calcule e informe os seus vizinhos, ou seja, o número anterior e posterior.
    num = Number(prompt("Digite um número: "));

    alert(`O sucessor de ${num} é ${num + 1} e o anterior é ${num - 1}`);
}