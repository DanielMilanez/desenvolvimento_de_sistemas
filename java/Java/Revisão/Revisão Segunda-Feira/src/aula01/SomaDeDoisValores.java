package aula01;

import java.util.Scanner;

public class SomaDeDoisValores {
    public static void main(String[] args) {
        Scanner Keyboard = new Scanner(System.in);
        double FirstValue = Keyboard.nextDouble();
        double SecondValue = Keyboard.nextDouble();
        
        double Result = FirstValue + SecondValue;
        
        System.out.format("%.2f\n", Result);
        System.out.print("A media total e: ");
        System.out.format("%.2f\n", Result / 2);
        
    }
}
