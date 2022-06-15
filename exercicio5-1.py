
print('=-+=' * 18)

n = int(input('qual é o fatorial ? '))

c = n

f = 1

print('Calculando {}! = '.format(n), end='')

while c > 0:
    print('{}'.format(c), end='')
    #print(' x ' if c > 1 else ' = ', end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f = f * c
    c = c - 1

print('{}'.format(f))

print('=-+=' * 18)
