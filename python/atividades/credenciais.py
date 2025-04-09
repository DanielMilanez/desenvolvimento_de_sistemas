NOME  = input("Informe seu nome: ")
EMAIL = input("Informe seu e-mail: ")
SENHA = input("Informe sua senha: ")

pessoa = {
    'name': NOME,
    'email': EMAIL,
    'senha': SENHA
}
print("--" * 30)
print(f'\033[32m Credenciais cadastradas\033[m \n \
    Nome de usuário: {pessoa['name']} \n \
    Email de usuário {pessoa['email']} \n \
    Senha: {pessoa['senha']}') 
