package aula01;

import java.util.Scanner;

public class Baskara {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        System.out.print("Insira o valor de A: ");
        float A = keyboard.nextFloat();
        System.out.print("Insira o valor de B: ");
        float B = keyboard.nextFloat();
        System.out.print("Insira o valor de C: ");
        float C = keyboard.nextFloat();
        
        float delta = (float)Math.pow(B, 2) - 4 * A * C;
        
        if (delta > 0){
            double X1 = (-B + Math.sqrt(delta)) / 2 * A;
            double X2 = (-B - Math.sqrt(delta)) / 2 * A;
            
            System.out.format("Valor de delta: %.2f\n", delta);
            System.out.format("Valor de X1: %.2f\n", X1);
            System.out.format("Valor de X2: %.2f\n", X2);
        }
        else System.out.println("Nao existe raiz!");      
    }
}
