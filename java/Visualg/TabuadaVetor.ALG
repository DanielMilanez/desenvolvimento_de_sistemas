Algoritmo "TabuadaVetor"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 23/04/2025
Var
// Se��o de Declara��es das vari�veis 
numI,numM: inteiro
numT: vetor[1..10] de inteiro
res: vetor[1..10] de inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreva("Digite um numero: ")
leia(numM)

para numI <- 1 ate 10 faca
   numT[numI]<- numI
   res[numI] <-  numM * numT[numI]
   escreval(numM," X ",numT[numI]," =",res[numI])
fimpara

Fimalgoritmo