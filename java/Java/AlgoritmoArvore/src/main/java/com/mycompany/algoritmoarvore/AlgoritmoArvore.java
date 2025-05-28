/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.algoritmoarvore;

import java.util.Scanner;

/**
 *
 * @author ead
 */
public class AlgoritmoArvore {
    public static void main(String[] args) {
        Scanner ln = new Scanner(System.in);
        
        System.out.print("Quantas linhas vc deseja: ");
        int lines = ln.nextInt();

        System.out.println("\n--------------------");
        
        for (int i = 1; i <= lines; ++i){
            System.out.print("\n");   
            for (int j = 1; j <= i; ++j){
                System.out.print("*");
            }
        }
        
        System.out.println("\n--------------------");
        
        for(int i = 1; i <= lines; i++){
            for(int j = 1; j <= (lines - i); j++) System.out.print(" ");            
            for(int k = 1; k <= i; k++) System.out.print("*");
            
            System.out.println(); 
        }
        
        System.out.println("\n--------------------");
        
        for(int i = 1; i <= lines; i++){
            for(int j = 1; j <= (lines - i); j++) System.out.print(" ");
            for(int k = 1; k <= i; k++)System.out.print("#");
            
            System.out.print(" | ");
           
            for(int k = 1; k <= i; k++) System.out.print("*");
            System.out.println();
        }
        
        System.out.println("\n--------------------");
    }
}
