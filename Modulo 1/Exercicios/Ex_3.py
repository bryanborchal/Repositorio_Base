# Utilize um loop while e um loop for para adicionar itens na lista.
# Peça para que o usuário digite quantos filmes deseja adicionar, e também os nomes dos filmes



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

filmes = [] # Não apague esta lista
quantidade = int(input('quantos filmes deseja adicionar? '))

# LOOP WHILE
# i = 0
# while i < quantidade:
#     filme = input(f'Nome do {i+1}° filme: ')
#     filmes.append(filme)
#     i += 1

# print(filmes)





# LOOP FOR
for i in range(quantidade):
    filme = input(f'Nome do {i+1}° filme: ')
    filmes.append(filme)
print(filmes) 



