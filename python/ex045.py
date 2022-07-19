from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas opções: 
[ 0 ] PEDRA 
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
op = int(input('Qual é a sua jogada: '))
print('-=' * 11)
print('Computador jogou {}'.format(itens[pc]))
print('jogador jogou {}'.format(itens[op]))
print('-=' * 11)
if pc == 0:
    if op == 0:
        print('\033[33mEMPATE!')
    elif op == 1:
        print('\033[32mJOGADOR VENCE!')
    elif op == 2:
        print('\033[31mCOMPUTADOR VENCE!')
    else:
        print('\033[31mJOGADA INVÁLIDA!')
elif pc == 1:
    if op == 0:
        print('\033[31mCOMPUTADOR VENCE!')
    elif op == 1:
        print('\033[33mEMPATE!')
    elif op == 2:
        print('\033[32mJOGADOR VENCE!')
    else:
        print('\033[31mJOGADA INVÁLIDA!')
elif pc == 2:
    if op == 0:
        print('\033[32mJOGADOR VENCE!')
    elif op == 1:
        print('\033[31mCOMPUTADOR VENCE!')
    elif op == 2:
        print('\033[33mEMPATE!')
    else:
        print('\033[31mJOGADA INVÁLDA!')
else:
    print('\033[31mNÚMERO INVÁLIDO! Tente novamente....')
