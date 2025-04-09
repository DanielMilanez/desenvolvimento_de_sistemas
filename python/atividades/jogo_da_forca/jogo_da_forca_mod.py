from random import randint
from os import system
from lista_temas import temas

def sorteio(select_tema):
    system('cls')

    if select_tema in temas:
        palavra = temas[select_tema][randint(0, len(temas[select_tema]) - 1)]
        return palavra, select_tema
    else:
        return False, None

def mostrar_temas():
    print("Temas existentes:")
    for indice, tema in enumerate(temas.keys(), start=1):
        print(f"{indice} - {tema.capitalize()}")
    print('=' * 30)

def game():
    print('=' * 30)
    mostrar_temas()
    
    while True:
        palavra_chave_input = input('Digite o tema: ').lower()
        palavra_chave, tema = sorteio(palavra_chave_input)

        while palavra_chave == False:
            system('cls')
            print('=' * 30)
            mostrar_temas()
            palavra_chave_input = input('\033"[31mTema inválido\033[m digite um tema: ').lower().strip()
            palavra_chave, tema = sorteio(palavra_chave_input)
            
        fim = game_core(palavra_chave, tema)
        if fim == True:
            break

def game_core(palavra_chave, tema):
    vida = 6
    letra_digitada = set()
    try_count = 0
    mesma_letra = False
    
    while True:
        print(f'Você escolheu \033[32m{tema}!\033[m')
        print('Digitados >>', end=' ')
        
        for letra in letra_digitada:
            print(letra, end=', ')
            
        print()
        print('=' * 30)
        
        # Desenhando
        for letra in palavra_chave:
            if letra in letra_digitada:
                print(letra, end=' ')
            else:
                if letra == ' ':
                    print('-', end=' ')
                else:
                    print('_', end=' ')

        tentativa = input('Seu palpite >> ').lower()
        if tentativa in letra_digitada:
            system('cls')
            print('\033[31mEssa letra já foi digitada!\033[m')
            mesma_letra = True
        else:
            mesma_letra = False
            letra_digitada.add(tentativa)
        
            if tentativa not in palavra_chave:
                system('cls')
                vida -= 1
                print('Você \033[31mERROU\033[m! Tente novamente')
                print(f'Você possui {vida} tentativas')
                print('=' * 30)
            else:
                if mesma_letra == False:
                    system('cls')
        
        if vida <= 0:
            print(f'Você perdeu, você não conseguiu adivinhar a palavra correta, ela era \033[31m{str(palavra_chave).upper()}\033[m')
            return True
        
        if vida == 3:
            while True:
                select = input('Você deseja uma dica em troca de uma vida? (s/n) ')                
                match select:
                    case 's':
                        vida -= 1
                        selections = randint(0, len(palavra_chave) - 1)

                        while palavra_chave[selections] in letra_digitada:
                            selections = randint(0, len(palavra_chave) - 1)

                        nova_letra = palavra_chave[selections]
                        letra_digitada.add(nova_letra)

                        system('cls')
                        print(f'Você possui {vida} tentativas')
                        print(f'\033[33mSua dica é: {nova_letra}\033[m')
                        print('=' * 30)
                        break
                    
                    case 'n':
                        break
                 
        if tentativa == palavra_chave:
            print('=' * 30)
            print(f'\033[33mVocê ganhou!\033[m Em {try_count} tentativas!')
            print('=' * 30)   
            return True
        
        try_count += 1  
        