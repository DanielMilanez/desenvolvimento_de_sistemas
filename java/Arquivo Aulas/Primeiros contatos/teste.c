#include <stdio.h>
#include <math.h>

#define WIDTH 40
#define HEIGHT 20
#define R1 1.0    // Raio maior (do centro para o centro do tubo)
#define R2 0.3    // Raio menor (do centro do tubo para a borda)
#define K2 (5 * WIDTH)

void printDonut() {
    float A, B, i, j;
    float x, y, z, ooz, c, l;
    int p, q;
    
    for (j = 0; j < 628; j += 7) {  // 2*PI é aproximadamente 6.28
        for (i = 0; i < 628; i += 2) {  // 2*PI em intervalos menores
            c = sin(i); // Cálculo do cosseno
            l = cos(j); // Cálculo do seno
            
            // Coordenadas 3D do donut
            x = cos(i) * (R1 + R2 * c);
            y = sin(i) * (R1 + R2 * c);
            z = l * (R2 + R2 * c); // Calculando a profundidade do donut
            
            // Projeção para coordenadas 2D
            ooz = 1.0 / (z + 4);  // A perspectiva (aproximando as profundidades)
            p = (int)(WIDTH / 2 + K2 * ooz * x);
            q = (int)(HEIGHT / 2 - K2 * ooz * y);
            
            // Usando um array de intensidade de caracteres baseado na profundidade z
            if (q >= 0 && q < HEIGHT && p >= 0 && p < WIDTH) {
                int N = (int)(8 * ((l * c) - 0.5));
                if (N > 0) {
                    printf(".");
                } else if (N > -5) {
                    printf("+");
                } else if (N > -10) {
                    printf("o");
                } else if (N > -15) {
                    printf("*");
                } else if (N > -20) {
                    printf("0");
                } else {
                    printf(" ");
                }
            }
        }
        printf("\n");
    }
}

int main() {
    printf("Imprimindo um donut 3D no terminal:\n\n");
    printDonut();
    return 0;
}
