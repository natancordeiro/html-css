print('\033[1;34mHORA DO ALISTAMENTO!\033[m')
nasc = int(input('Ano de nascimento: '))
idade = 2022 - nasc
print('Você tem {} anos.'.format(idade))
if idade < 18:
    print('\033[32mAinda faltam {} anos para o alistamenento!\033[m'.format(18-idade))
    print('Seu alistamento será em {}.'.format(nasc+18))
elif idade == 18:
    print('\033[33mVocê tem que se alistar IMEDIATAMENTE!\033[m')
else:
    print('\033[31mVocê já deveria ter se alistado a {} anos!\033[m'.format(idade-18))
    print('Seu ano de alistamento foi em {}!'.format(nasc+18))