
package aula01;

import java.util.Scanner;

public class Atividade {
    public static void main(String[] args) {
        
        Scanner key = new Scanner(System.in);
        
        System.out.print("Informe uma op: ");
        int opition = key.nextInt();
        
        do{           
            switch(opition){
                case 1 -> {
                    Scanner Keyboard = new Scanner(System.in);
                    System.out.print("Informe o primeiro valor: ");
                    double FirstValue = Keyboard.nextDouble();
                    System.out.print("Informe o segundo valor: ");
                    double SecondValue = Keyboard.nextDouble();

                    double Result = FirstValue + SecondValue;

                    System.out.format("%.2f\n", Result);
                    System.out.print("A media total e: ");
                    System.out.format("%.2f\n", Result / 2);
                }

                case 2 -> {
                    System.out.print("Informe um valor para verificar a paridade: ");
                    Scanner keyboard = new Scanner(System.in);
                    int paridade = keyboard.nextInt();
                    String valueResponse = paridade % 2 == 0 ? "O numero e par" : "O numero e impar";

                    System.out.format("%s\n", valueResponse);    
                }

                case 3 -> {
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

                default ->{
                        System.out.println("Entrada invalida");
                    }
                }
            
            System.out.print("Informe uma op: ");
            opition = key.nextInt();
            
        } while (opition != -1);
        System.out.println("FIM DO PROGRAMA");
    }
}
