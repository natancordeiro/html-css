print('=-'*15)
print('{:^30}'.format('BANCO NATAN'))
print('=-'*15)
valor = int(input('Que valor você quer sacar? '))
total = valor
ced = 50
tced = 0
while True:
    if total >= ced:
        total -= ced
        tced += 1
    else:
        if tced > 0:
            print(f'Total de {tced} cédulas de R${ced}')
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tced = 0
        if total == 0:
            break
print('=-'*15)
print('Volte sempre ao BANCO NATAN! Tenha um bom dia.')