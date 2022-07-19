print('\033[1;33mPROGRAMA EMPRÉSTIMO BANCÁRIO\033[m')
casa = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o salário? R$'))
anos = float(input('Em quantos anos deseja pagar? '))
mes = casa / (anos * 12)
if mes > (sal*30/100):
    print('\033[1;31mSeu empréstimo foi NEGADO!!!')
    print('\033[1;31mA prestação ficaria R${:.2f}. Excedendo 30% do seu salário.\033[m.'.format(mes))
else:
    print('\033[1;32mSeu empréstimo foi APROVADO!\033[m')
    print('Você irá pagar R${:.2f} por mês.'.format(mes))
