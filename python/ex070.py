print('-'*18)
print('LEITOR DE PRODUTOS')
print('-'*18)
tot = 0
mais = 0
nomeprod = ' '
valorprod = 10000000
while True:
    nome = str(input('Qual o nome do produto? ')).strip()
    valor = float(input('Qual o valor dele? R$'))
    tot += valor
    if valor > 1000:
        mais += 1
    if valor < valorprod:
        valorprod = valor
        nomeprod = nome
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar in 'N':
        print('\033[32mPROGRAMA FINALIZADO!\033[m')
        break
print(f'O total do valor gasto foi R${tot:.2f}')
print(f'{mais} produtos custam mais de R$1000.00')
print(f'O produto mais barato é o {nomeprod}')
