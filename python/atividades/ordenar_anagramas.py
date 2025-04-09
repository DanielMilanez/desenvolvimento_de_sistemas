# Criar um programa que realize a ordenação de palavras em conjuntos se essas palavras forem iguais mesmo sendo anagramas

def is_anagram(num_repeat):
    words = []
    for i in range(num_repeat):
        words.append(input(f"{i + 1}° palavra >> "))

    grouped = []  
    for first_indice, first_word in enumerate(words):
        if any(first_word in group for group in grouped): 
            continue
        
        my_atual_set = [first_word]  
        for second_indice, second_word in enumerate(words):
            if first_indice != second_indice: 
                if sorted(first_word) == sorted(second_word):
                    my_atual_set.append(second_word)
        
        grouped.append(my_atual_set)  
        print(f"{len(grouped)}° Grupo: {my_atual_set}")

print("==" * 40)
num_repeat = int(input("Informe o valor de palavras a serem analisadas: "))
is_anagram(num_repeat)
print("==" * 40)

