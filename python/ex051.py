titulo = str('10 TERMOS EM PA')
print('='*28)
print(titulo.center(25, ' '))
print('='*28)
valor = int(input('Primeiro valor: '))
razao = int(input('Razão: '))
dec = valor + (10 - 1) * razao
for c in range(valor, dec, razao):
    print(c, end=' → ')
print('ACABOU!')
