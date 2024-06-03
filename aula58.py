# Definindo a frase
frase = 'Olha só que, coisa interessante'
print("Frase original:", frase)

# Dividindo a frase em partes usando vírgula como delimitador
lista_frases_cruas = frase.split(',')
print("Após split:", lista_frases_cruas)
# Resultado: ['Olha só que', ' coisa interessante']
# Formato: Lista de strings

# Removendo espaços em branco no início e no fim de cada parte
lista_frases = [parte.strip() for parte in lista_frases_cruas]
print("Após strip:", lista_frases)
# Resultado: ['Olha só que', 'coisa interessante']
# Formato: Lista de strings

# Unindo a lista de partes em uma única string, separada por vírgula e espaço
frases_unidas = ', '.join(lista_frases)
print("Após join:", frases_unidas)
# Resultado: 'Olha só que, coisa interessante'
# Formato: Única string
