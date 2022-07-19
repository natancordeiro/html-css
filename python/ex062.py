titulo = str('10 TERMOS EM PA')
print('='*28)
print(titulo.center(25, ' '))
print('='*28)
valor = int(input('Primeiro valor: '))
razao = int(input('Razão: '))
cont = 1
termo = valor
total = 0
maist = 10
while maist != 0:
    total += maist
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    maist = int(input('Quantos termos você quer ver a mais? '))
print('Progressão finazizada com {} termos mostrados.'.format(total))
