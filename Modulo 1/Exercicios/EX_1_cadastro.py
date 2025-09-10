# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('|',30*'-','|')
print('|',10*'-',"CADASTRO",10*'-','|')
print('|',30*'-','|')
nome = input("| Qual é o seu nome? ")
idade = input("| Qual é a sua idade? ")
email = input("| Qual é o seu email? ")
senha = input("| Qual é a sua senha? ")

print('|',30*'-','|')
print('|',5*'-',"USUÁRIO CADASTRADO",5*'-','|')
print("| Seja bem vindo(a)", nome+'!')
print("| Email:", email)
print('|',30*'-','|')