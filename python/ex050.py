v = 0
soma = 0
for c in range(0, 6):
    v += 1
    n = int(input('Digite o {}º valor: '.format(v)))
    if n % 2 == 0:
        soma += n
print('A soma entre os valores pares foi {}'.format(soma))
