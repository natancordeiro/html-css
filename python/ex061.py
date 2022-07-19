titulo = str('10 TERMOS EM PA')
print('='*28)
print(titulo.center(25, ' '))
print('='*28)
valor = int(input('Primeiro valor: '))
razao = int(input('Razão: '))
cont = 1
while cont <= 10:
    print('{} → '.format(valor), end= '')
    cont += 1
    valor += razao
print('FIM')
