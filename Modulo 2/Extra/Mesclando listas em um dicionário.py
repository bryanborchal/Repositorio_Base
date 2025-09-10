chaves = ["nome", "idade", "cidade"] 
valores = ["Ana", 25, "Rio de Janeiro"]

dicionario = {}
for i in range(len(chaves)):
    dicionario[chaves[i]] = valores[i]
print(dicionario)