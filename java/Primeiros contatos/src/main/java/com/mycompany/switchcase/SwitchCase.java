/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.switchcase;

/**
 *
 * @author ead
 */

import java.util.Scanner;
import javax.swing.JFrame;
import javax.swing.JOptionPane;

public class SwitchCase {
    public static void main(String[] args) {        
        Scanner op = new Scanner(System.in);
        JFrame frame = new JFrame();
        frame.setAlwaysOnTop(true);
        
        System.out.println("  _____________________ ");
        System.out.print(" | Informe sua escolha |\n");
        System.out.print(" |_____________________|\n");
        System.out.print(" [0] - Verificar par ou impar\n");
        System.out.print(" [1] - Baskara\n");
        System.out.print(" [2] - Verificar idade\n---------------------\n >> ");
        
        int escolha = op.nextInt();
        
        switch(escolha){
            case 1 -> {
                System.out.print("Informe um número: ");
                int n1 = op.nextInt();
                
                String result = (n1 % 2 == 0) ? "Par" : "Impar";
                
                String finalResult = String.format("O numero %d é: %s ", n1,
                                                    result);
                
                JOptionPane.showMessageDialog(null, finalResult, "Resposta",
                                              JOptionPane.PLAIN_MESSAGE);
                        
            }
                
            case 2 -> {
                double a, b, c, x1, x2, delta;
                System.out.print("Informe os valores de A: ");
                a = op.nextDouble();
                
                System.out.print("Informe os valores de B: ");
                b = op.nextDouble();
                
                System.out.print("Informe os valores de C: ");
                c = op.nextDouble();
                
                delta = Math.pow(b, 2) - 4 * a * c;
                x1 = (-b + Math.sqrt(delta)) / 2 * a;
                x2 = (-b - Math.sqrt(delta)) / 2 * a;
                
                System.out.format("Delta: %.2f \nX1: %.2f \nX2 %.2f", delta,
                                    x1, x2);
            }
            
            case 3 -> {
                System.out.print("Informe sua idade: ");
                int idade = op.nextInt();
                
                if (idade <= 0) System.out.println("Entrada inválida!");
                else if (idade < 18) System.out.println("Vc nao pode votar");
                
                else if (idade >= 18 && idade < 65) System.out.println("Vc eh"
                        + "obrigado a votar");
                
                else if (idade >= 65) System.out.println("Voce não é obrigado"
                        + "a votar");
            }
                
            default -> {
                System.out.println("Opição inválida, tente novamente!");
            }
        }
    }
}
