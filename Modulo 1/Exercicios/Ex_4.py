# Calcule a média das notas utilizando um loop while e também um loop for


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

notas = ['9.5', '10', '6.75', '5.5']

# LOOP WHILE
i = 0
soma = 0.0
while i < len(notas):
    soma += float(notas[i])
    i += 1

media1 = soma/len(notas)
print(f'{media1:.2f}')






# LOOP FOR
#soma = 0.0
#for i in notas:
#    soma += float(i)
#    media = soma/len(notas)
#
#print(f'{media:.2f}')
    


