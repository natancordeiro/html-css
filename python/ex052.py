n = int(input('Digite um número: '))
cont = 0
p = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[31m', end=' ')
        cont += 1
    else:
        print('\033[m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(n, cont))
if cont <= 2:
    print('Ele é PRIMO!')
else:
    print('Ele NÃO É PRIMO!')