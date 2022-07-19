from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
r = 0
opc = 0
while opc != 5:
    opc = int(input('''[ 1 ] Somar
[ 2 ] multiplicar 
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Qual é a sua opção: '''))
    if opc == 1:
        r = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, r))
        print('=-'*20)
        sleep(1.5)
    elif opc == 2:
        r = n1 * n2
        print('A multiplicação entre {} e {} é {}'. format(n1, n2, r))
        print('=-'*20)
        sleep(1.5)
    elif opc == 3:
        if n1 > n2:
            r = n1
        else:
            r = n2
        print('O maior número entre {} e {} é o {}'.format(n1, n2, r))
        print('=-'*20)
        sleep(1.5)
    elif opc == 4:
        print('\033[34m---Novos números---\033[m')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opc == 5:
        print('Finalizando...')
    else:
        print('\033[31mOpção inválida! Tente novamente...\033[m')
        sleep(1.5)

sleep(2.5)
print('PROGRAMA FINALIZADO')