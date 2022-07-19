tidade = 0
maior = 0
nomemaisvelhro = ''
menor20 = 0
for c in range(1, 5):
    print('{}º pessoa: '.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().upper()
    tidade += idade
    if c == 1 and sexo[0] == 'M':
        maior = idade
        nomemaisvelho = nome
    if sexo[0] == 'M' and idade > maior:
        maior = idade
        nomemaisvelho = nome
    if sexo[0] == 'F' and idade < 20:
        menor20 += 1
media = tidade / 4
print('A média de idade do grupo é de {}'.format(media))
print('O homem mais velho é o {} com {} anos'.format(nomemaisvelho.title(), maior))
print('Ao todo são {} mulheres com menos de 20 anos de idade'.format(menor20))
