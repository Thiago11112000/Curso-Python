



lista = [10,20,30,40]
# lista[2] = 300
# del lista[2]
# numero = lista[2]
# print(lista)
# print(numero)

lista.append(50)
lista.pop() # remove o último
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido', ultimo_valor)

