// � poss�vel trabalhar com caracteres especiais utilizados na lingua portugesa
#include <stdio.h>
#include <locale.h>

int main(void) {
    setlocale(LC_ALL, "Portuguese_Brazil");
    
    float teste = 1.5;

    printf("Opi��es para a escrita, o �nico problema � a digita��o de n�meros com virgula, pois, com esta lib ele troca o . para uma ,");
    printf("Exemplo: %.2f", teste);
}