"""
iterável > str, range, etc
iterador -> quem sabe entregar um valor por vez
next -> me entegue o próximo valor
inter -> me entregue o seu iterador
"""
# texto = iter('Luiz') # __iter__() #__next__()

# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))


texto = 'Luiz' # iterável
# iterador = iter(texto) # iterador

for letra in texto:
    print(letra)

# while True:
#     try:
#         print(next(iterador))

#     except StopIteration:
#         break






