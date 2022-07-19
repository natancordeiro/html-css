numero = ('zero', 'um', 'dois', 'três', 'quatro',
          'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
          'onze', 'doze', 'treze', 'quatorze', 'quinze',
          'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número entre 0 e 20: '))
while True:
    if 0 <= num <= 20:
        break
    num = int(input('\033[31mTente novamente!\033[m Digite um número entre 0 e 20: '))
print(f'Você digitou o número \033[1;34m{numero[num]}')
