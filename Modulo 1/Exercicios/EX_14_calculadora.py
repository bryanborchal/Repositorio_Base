# Escreva um código que mostre na tela um "MENU" de opções de operações matematicas (Adição, Subtração, Divisão e Multiplicação)
# O usuário deve escolher uma das opções e depois inserir dois números para serem calculados de acordo com a operação escolhida.
# No fim mostre o resultado da operação

# OUTPUT ESPERADO:

#----------------------------------------- Exemplo 1 (Soma)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 1
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 20.0

# ----------------------------------------- Exemplo 2 (Multiplicação)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 3
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 100.0

# ----------------------------------------- Exemplo 3 (Opção inválida)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 6
# | Digite o primeiro número:1
# | Digite o segundo número:2
# | ERRO. Escolha uma opção válida.



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('|',30*'-','|')
print('| Calculadora')
print('|',30*'-','|')
print('| 1 - Soma')
print('| 2 - Subtração')
print('| 3 - Multiplicação')
print('| 4 - Divisão')
print('|',30*'-','|')
opcoes = int(input('| Escolha uma das opções: '))

if opcoes == 1:
    numero_1 = float(input('| Digite o primeiro número: '))
    numero_2 = float(input('| Digite o segundo número: '))
    soma = numero_1+numero_2
    print(f'| O resultado é: {soma}')
elif opcoes == 2:
    numero_3 = float(input('| Digite o primeiro número: '))
    numero_4 = float(input('| Digite o segundo número: '))
    subtracao = numero_3-numero_4
    print(f'| O resultado é: {subtracao}')
elif opcoes == 3:
    numero_5 = float(input('| Digite o primeiro número: '))
    numero_6 = float(input('| Digite o primeiro número: '))
    multiplicacao = numero_5*numero_6
    print(f'| O resultado é: {multiplicacao}')
elif opcoes == 4:
    numero_7 = float(input('| Digite o primeiro número: '))
    numero_8 = float(input('| Digite o primeiro número: '))
    divisao = numero_7/numero_8
    print(f'| o resultado é: {divisao}')
else:
    print('| ERRO. Escolha uma opção válida.')

