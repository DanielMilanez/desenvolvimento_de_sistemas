from re import sub

def its_palindrome(word):
    clean_word = sub(r'[^a-zA-Z0-9]', '', word).lower() 

    if clean_word == clean_word[::-1]:
        return True
    return False

print("É um palíndromo?")
print("-" * 30)

# Variáveis constantes possuem todos os caracteres maúsculos, nos as utilizamos para quando não queremos que essa variável tenha alteração
VERIFY = its_palindrome(input("Informe a palavra ou uma frase: "))
response = print("Sim, é um palíndromo") if VERIFY else print("Não, é um palíndromo")
