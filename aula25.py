"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da strf
"""
variavel = 'Olá mundo'
teste = len(variavel)
print (teste)
print(variavel[4:8]) # fatiamento : indo até o final
                     # omite o inicio e o final sempre
                     # colocando 1 a mais 
print(variavel[0:9:4])
print(variavel[::-1]) #Inversão
print(variavel[-1:-10:-1])# Inversão #2 a mais