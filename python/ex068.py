from random import randint

par = 'PAR'
impar = 'IMPAR'
c = 0
print('    PAR OU IMPAR\n', '-'*20)
while True:
    nj = int(input('Digite um número de 0 a 10: '))
    nc = randint(0, 10)

    if nj % 2 == 0:
        print('Você jogou um número PAR')
        nj = par
    elif nj % 2 == 1:
        print('Você jogou um número IMPAR')
        nj = impar
    if nc % 2 == 0:
        print(f'O computador jogou um número PAR ({nc})')
        nc = par
    elif nc % 2 == 1:
        print(f'O computador jogou um número IMPAR ({nc})')
        nc = impar
    if nj != nc:
        break
    c += 1
    print('\033[32mAcertou! continue...\033[m')
print(f'\033[31mVocê perdeu!\033[m\nVocê acertou {c} vezes consecutivas. Parabéns!')
