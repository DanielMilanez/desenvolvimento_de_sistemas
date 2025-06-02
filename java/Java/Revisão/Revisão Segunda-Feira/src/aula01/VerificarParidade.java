package aula01;

import java.util.Scanner;

public class VerificarParidade {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        int paridade = keyboard.nextInt();
        String valueResponse = paridade % 2 == 0 ? "O numero e par" : "O numero e impar";
        
        System.out.format("O numero e: %s\n", valueResponse);        
    }
}
