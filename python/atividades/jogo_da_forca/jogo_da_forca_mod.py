from random import randint
from os import system

tema = ''

def sorteio(select_tema):
    system('clear')
    frutas = ['melancia', 'pessego', 'manga', 'pera', 'morango']
    animais = ['porco', 'cabra', 'galinha', 'vaca', 'baleia']
    cep = ['barcelona', 'bugaria', 'argelhia', 'armenia', 'brasil']

    sorteio = randint(0, 4)

    match select_tema:
        case 'frutas':
            tema = 'frutas'
            palavra = frutas[sorteio]
            return palavra, tema
        case 'animais':
            tema = 'animais'
            palavra = animais[sorteio]
            return palavra, tema
        case 'cep':
            tema = 'cep'
            palavra = cep[sorteio]
            return palavra, tema
        case _: 
            return False
        
def game():
    print('=' * 30)
    print('Temas existentes', end=' ')
    print('\n - Animais \n - CEP \n - Frutas')
    
    while True:
        palavra_chave = input('Digite o tema: ').lower()
        palavra_chave, tema = sorteio(palavra_chave)
            
        while palavra_chave == False:
            system('cls')
            print('=' * 30)
            print('Temas existentes', end=' ')
            print('\n - Animais \n - CEP \n - Frutas')
            print('=' * 30)

            palavra_chave = input('\033[31mTema inválido\033[m, digite um tema: ').lower().strip()
            palavra_chave = sorteio(palavra_chave)
            
        fim = game_core(palavra_chave, tema)
        if fim == True:
            break
            
def game_core(palavra_chave, tema):
    vida = 6
    letra_digitada = set()
    try_count = 0
    
    while True:
        print(f'Você escolheu \033[32m{tema}!\033[m')
        print('Letras digitadas >>', end=' ')
        
        for letra in letra_digitada:
            print(letra, end=', ')
            
        print()
        print('=' * 30)
        
        # Desenhando
        for letra in palavra_chave:
            if letra in letra_digitada:
                print(letra, end=' ')
            else:
                print('_', end=' ')

        tentativa = input('Seu palpite >> ').lower()
        if tentativa in letra_digitada:
            print('Essa letra já foi digitada!')
        else:
            letra_digitada.add(tentativa)
        
        if tentativa not in palavra_chave:
            system('cls')
            vida -= 1
            print('Você \033[31mERROU\033[m! Tente novamente')
            print(f'Você possui {vida} tentativas')
            print('=' * 30)
        
        if vida <= 0:
            print(f'Você perdeu, você não conseguiu adivinhar a palavra correta, ela era {palavra_chave}')
            return True
        
        if vida == 3:
            while True:
                select = input('Você deseja uma dica em troca de uma vida? (s/n) ')
                
                match select:
                    case 's':
                        vida -= 1
                        selections = randint(0, len(palavra_chave))
                        
                        while selections in letra_digitada:
                            selections = randint(0, len(palavra_chave))
                            
                        nova_letra = palavra_chave[selections]
                        letra_digitada.add(nova_letra)
                        system('cls')
                        print(f'Você possui {vida} tentativas')
                        break
                    
                    case 'n':
                        break
                
        if tentativa == palavra_chave:
            print('=' * 30)
            print(f'\033[33mVocê ganhou!\033[m Em {try_count} tentativas!')    
            return True
        
        try_count += 1  
    