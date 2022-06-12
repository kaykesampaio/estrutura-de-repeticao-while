
print('-=-' * 20)

from time import sleep

n1 = int(input('Primeiro valor: '))

n2 = int(input('Segundo valor: '))

opção = 0

while opção != 5:
    print('''    MENU
    [ 1 ] Somar
    [ 2 ] Multiplicar 
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do progama''')

    opção = int(input('>>>>> Qual é sua opção? '))

    sleep(1)

    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}.'.format(n1, n2, soma))

    elif opção == 2:
        mult = n1 * n2
        print('Multiplicando {} x {} é {}'.format(n1, n2, mult))

    elif opção == 3:
        if n1 > n2:
            print('Entre os valores {} e {} o maior é {}'.format(n1, n2, n1))
        elif n1 < n2:
            print('Entre os valores {} e {} o menor é {}'.format(n1, n2, n2))
        else:
            print('Ambos são iguais, não há um valor maior ou menor!')

    elif opção == 4:
        print('Informe os numeros novamente:')

        n1 = int(input('Primeiro valor: '))

        n2 = int(input('Segundo valor: '))

    elif opção == 5:
        print('Finalizando...')
        sleep(1)

    else:
        print('Opção invalida. Tente novamente')
    print('-=-' * 20)

print('Fim do progama! Volte sempre!')

print('-=-' * 20)

