num = int(input('Informe um número: '))
#numero = str(num)
#print('Unidade: {}'.format(numero[3]))
#print('Dezena: {}'.format(numero[2]))
#print('Centena: {}'.format(numero[1]))
#print('Milhar: {}'.format(numero[0]))
unid = num // 1 % 10
dez = num // 10 % 10
cent = num // 100 % 10
mil = num // 1000 % 10
print('Unidade: {}'.format(unid))
print('Dezena: {}'. format(dez))
print('Centena: {}'.format(cent))
print('Milhar: {}'.format(mil))
