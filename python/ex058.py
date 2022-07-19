import random

nr = (random.randint(0, 10))
print('JOGO DO COMPUTADOR\nAcabei de pensar em um número de 0 a 10.\nSerá que você consegue advinhar qual foi?')
nj = int(input('Qual o seu palpite? '))
palp = 1
while nj != nr:
    if nj > nr:
        print('Menos...')
    else:
        print('Mais...')
    nj = int(input('Tente novamente: '))
    palp += 1
print('\033[32mVocê acertou!\033[m\nVocê tentou {} vezes.'.format(palp))
