'''
Itrando strings com while
'''
#       01234567890
nome = 'Luiz otávio' # iteráveis

# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[3])

nova_string = ''

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    print(nome[indice])
    novo_nome += f'*{letra}'
    indice+=1

novo_nome += '*'
print(novo_nome)


