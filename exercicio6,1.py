print('\n')

print(' 👇' * 24)

print('Gerador de PA')

print('=-+=' * 18)

p = int(input('Primeiro termo: '))

r = int(input('razão: '))

termo = p

cont = 1

total = 0

mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ➟  '.format(termo), end='')
        termo = termo + r
        cont = cont + 1

    print('PAUSA')

    mais = int(input('Quantos termos você quer mostrar a mais? '))

print('progressão finalizada com {} termos mostrados'.format(total))

print('FIM')

print('=-+=' * 18)

print('\n')
