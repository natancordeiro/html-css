print('-'*17)
print('Análise de dados')
print('-'*17)
cont = 1
mais18 = 0
homens = 0
mul20 = 0
while True:
    idade = int(input(f'Qual a idade da {cont}º pessoa? '))
    sexo = str(input(f'Qual o sexo da {cont}º pessoa? ')).strip().upper()
    cont += 1
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mul20 += 1
    c = str(input('Quer continuar? [S/N] ')).strip().upper()
    if c == 'N':
        break
print(f'Ao todo temos {mais18} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {homens} homens.')
print(f'Temos {mul20} mulheres com menos de 20 anos cadastradas.')
print('\033[1;34mOBRIGADO POR USAR O NOSSO PROGRAMA!\033[m')