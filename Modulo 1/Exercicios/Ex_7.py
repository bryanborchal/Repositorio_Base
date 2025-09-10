# Crie uma lista com 3 dicionários, cada um representando uma pessoa (contendo nome, idade, cidade). Use um laço para imprimir o nome de cada pessoa.



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
lista = [
    {
        'Nome': 'Andyribfer',
        'Idade':18,
        'Cidade':'São Paulo'
    },
    {
        'Nome':'Bryan',
        'Idade':17,
        'Cidade':'Santa Catarina'
    },
    {
        'Nome':'Joãozinho',
        'Idade':32,
        'Cidade':'Acre'
    }
]

for i in lista:
    print(i['Nome'])