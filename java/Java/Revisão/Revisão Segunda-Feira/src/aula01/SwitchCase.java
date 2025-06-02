package aula01;

import java.util.Scanner;

public class SwitchCase {

    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        System.out.println("Quantas pernas? ");
        int perna = keyboard.nextInt();
        String tipo ;
        
        System.out.println("Isso eh um(a)");
        
        tipo = switch (perna) {
            case 1 -> "SACI";
            case 2 -> "BIGODE";
            case 3 -> "TRIPE";
            case 4 -> "QUADRUPEDE";
            case 6 -> "ARANHA";
            default -> "ET";
        };
        
        System.out.println(tipo);
    }
    
}
