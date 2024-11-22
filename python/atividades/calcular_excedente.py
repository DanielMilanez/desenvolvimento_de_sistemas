peso_peixe = float(input("Informe o valor em Kg do total pescado: "))
response = print(f"Multa de {(peso_peixe - 50) * 4}") if peso_peixe > 50 else print("Valor abaixo do limite")
