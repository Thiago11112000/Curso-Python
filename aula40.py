""" while/else"""

string = 'Valor qualquer'

i = 0
while 1 < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i +=1
    
else:
    print("Não encontrei um espaço na string")
print('fora do while')    