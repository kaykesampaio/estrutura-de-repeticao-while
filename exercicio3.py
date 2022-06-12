
from random import randint

computador = randint(0, 10)

print('Sou seu computador ... acabei de pensar em um número entre 0 e 10.')

print('Será que você consegue adivinhar qual foi?')

acertou = False

palpites = 0

while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites = palpites + 1
    if jogador == computador:
        acertou = True
    else: 
        if jogador < computador:
            print('Mais... Tente de novo outro valor!')
        elif jogador > computador:
            print('Menos... Tente de novo outro valor')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))

