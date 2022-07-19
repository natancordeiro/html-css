v = 0
maiores = 0
menores = 0
for c in range(1, 8):
    v += 1
    ano = int(input('Ano de nascimento da {}º pessoa: '.format(v)))
    idade = 2022 - ano
    if idade <= 18:
        menores += 1
    else:
        maiores += 1
print('Dentre as 7 pessoas, {} são menores e {} já são maiores de idade!'.format(menores, maiores))