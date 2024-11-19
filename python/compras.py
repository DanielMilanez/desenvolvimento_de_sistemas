item_price = {
    'a': ['PAMONHA', 7.00],
    'b': ['CALDO', 4.50],
    'c': ['PASTEL', 6.99],
    'd': ['CAFÉ', 1.00],
}

for item in item_price:
    print(f"{item}) {item_price[item][0]} - {item_price[item][1]}")

def add_item(opition):
    total_value = item_price[opition][1]   
    return total_value 

opition = input("Informe uma opição: ").lower()
print(f"O valor total da sua compra é: R${add_item(opition)}")
