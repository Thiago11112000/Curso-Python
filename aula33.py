'''
Repetições
while(enquanto)
Executa uma ação enquanto uma condicção for verdadeira
'''

condicao = True
while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')
    if nome == 'sair':
        break

print('acabou')
