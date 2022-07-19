ano = int(input('Ano de nascimento: '))
idade = 2022 - ano
if idade < 9:
    print('Você tem {} anos e está na categoria MIRIM!'.format(idade))
elif 10 < idade < 14:
    print('Você tem {} anos e está na categoria INFANTIL!'.format(idade))
elif 15 < idade < 19:
    print('Você tem {} anos e está na categoria JÚNIOR!'.format(idade))
elif 20< idade < 25:
    print('Você tem {} anos e está na categoria SÊNIOR!'.format(idade))
elif idade > 26:
    print('Você tem {} anos e está na categoria MASTER!'.format(idade))
