Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 23/04/2025
Var
// Se��o de Declara��es das vari�veis 
val: vetor[1..7] de inteiro
i, TotPar: inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
TotPar <- 0
para i <- 1 ate 7 faca
  escreval("Digite o ",i,"�. valor: ")
  leia(val[i])
  se(val[i] % 2 = 0)entao
     TotPar <- TotPar +1
  fimse
fimpara
escreval("O total de pares foram ",TotPar)

Fimalgoritmo