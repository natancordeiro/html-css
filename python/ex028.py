import random
nr = (random.randint(0,5))
nu = int(input('Digite um número de 0 a 5: '))
if nu == nr:
    print('Parabéns, você venceu!')
else:
    print('Não foi dessa vez!')
    print('O número pensado pelo computador foi {}'.format(nr))
