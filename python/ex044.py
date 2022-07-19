valor = float(input('Qual o valor do produto? '))
op = int(input('''FORMA DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mias no cartão
Digite uma opção: '''))
desc = 0
pc = 0
if op == 1:
    desc = valor - (valor*10/100)
    print('Pagando à vista você tem 10% de desconto no valor do produto!\nVocê irá pagar R${:.2f}'.format(desc))
elif op == 2:
    desc = valor - (valor*5/100)
    print('Pagando à vista no cartão você tem 5% de desconto no valor do produto!\nVocê irá pagar R${:.2f}'.format(desc))
elif op == 3:
    pc = valor / 2
    print('Pagando em até 2x no cartão você pagará o valor formal de R${:.2f} em 2x de R${:.2f}'.format(valor, pc))
elif op == 4:
    desc = valor + (valor*20/100)
    qtpc = int(input('Em quantas vezes irá parcelar? '))
    pc = desc / qtpc
    print('Pagando em 3x no cartão ou mais, você pagará um juros de 20% do valor total do produto!')
    print('Você irá pagar R${:.2f} em {}X de R${:.2f}'.format(desc, qtpc, pc))
else:
    print('\033[31mNÚMERO INVALIDO! Tente novamente...\033[m')