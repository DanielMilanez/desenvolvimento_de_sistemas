idade = int(input("Informe o valor da sua idade: "))
print("Criança" if idade <= 15 else "Jovem" if idade < 30 else "Adulto" if idade < 60 else "Idoso")
