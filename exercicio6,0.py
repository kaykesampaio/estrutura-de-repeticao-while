print('\n')

print(' 👇' * 24)

print('Gerador de PA')

print('=-+=' * 18)

p = int(input('Primeiro termo: '))

r = int(input('razão: '))

termo = p

cont = 1

while cont <= 10:
    print('{} ➟  '.format(termo), end='')
    termo = termo + r
    cont = cont + 1

print('FIM')

print('=-+=' * 18)

print('\n')
