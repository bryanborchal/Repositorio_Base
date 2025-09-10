import csv

cadastro = [
    ["nome","idade","e-mail","senha"]
]

with open('cadastros.csv', 'a', newline='', encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow([cadastro])

print('|',30*'-','|')
print('| ---------- CADASTRO ---------- |')
print('|',30*'-','|')

nome = input('nome: ')
idade = input('idade: ')
email = input('e-mail: ')
senha = input('senha: ')

with open('cadastros.csv', 'a', newline='', encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow([nome,idade,email,senha])

print('|',30*'-','|')
print('| ---------- INFORMA ---------- |')
print('|',30*'-','|')
print('nome: ', nome)
print('idade: ', idade)
print('email: ', email)
print('senha: ', senha)
print('|',48*'-','|')
print('| -------- USUARIO CADASTRADO COM SUCESSO -------- |')
print('|',48*'-','|')
print('SEJA BEM VINDO(a) ' ,nome)