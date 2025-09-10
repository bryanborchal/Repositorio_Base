# Utilizando tanto um loop while quanto um loop for, escreva um código que exiba na tela o resultado abaixo:

#ID: 354 | Aluno: Fabrício
#ID: 847 | Aluno: Leandro
#ID: 195 | Aluno: Marcela


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
lista = ['Fabrício', 'Leandro', 'Marcela', [354, 847, 195, 0]] # Não apague e nem altere essa lista


# LOOP WHILE

#i = 0
#while i < len(lista)-1:
#    nome = lista[i]
#    id = lista[3][i]
#    i += 1
#    print(f'ID: {id} | Aluno: {nome}')



# LOOP FOR
i = 0
for i in range(len(lista)-1):
    nome = lista[i]
    id = lista[3][i]
    i += 1
    print(f'ID: {id} | Aluno: {nome}')


