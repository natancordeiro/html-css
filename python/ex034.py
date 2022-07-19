sal = float(input('Qual é o salário do funcionário? R$'))
if sal > 1250:
    sal = sal + (sal*10/100)
else:
    sal = sal + (sal*15/100)
print('O funcionário passará a receber R${:.2f}'.format(sal))
