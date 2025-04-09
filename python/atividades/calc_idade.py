from datetime import datetime as dt

ano_nascimento = input("Informe o ano que você nsaceu: ")
ano_atual = dt.now().year

print(f"Sua idade é: {ano_atual - int(ano_nascimento)}")
