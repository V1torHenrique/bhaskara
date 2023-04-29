from time import sleep

print('\n<<< Olá, seja bem vindo. >>> \n'
'\n- Este programa te ajudará',
'nos seus exercícios de Equação do Segundo Grau.')

sleep(1)

while True:
    print('\nVamos começar..')

    sleep(1.5)
    print('\n<<< Caso não lembre como seja a equação de segundo grau: ax^2 – bx + c = 0 >>>',
    '\n- Fórmula de Bháskara: (-b +- raiz de delta) / (2.a) >>',
    '\n- Fórmula Delta = (b^2) - 4.a.c >>.')

    print('\nSabendo disso, informe os valores respectivos de a, b e c (ax^2 + bx - c = 0):')
    a = float(input('Digite o valor de a: '))
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))

    delta = (b**2) - 4 * a * c
    raiz_delta = delta ** 0.5

    print('\nPensando..')
    sleep(1)
    print(f'\nSubstituindo os valores: {a}x^2 + {b}x - {c} = 0')

    if a == 0:
        print('Valor informado em "a" não pode ser zero, tente novamente.')

    elif delta < 0:
        print('Valor resultante no delta não possui raiz real.')

    else:
        x1 = (-b + raiz_delta) / (2 * a)
        x2 = (-b - raiz_delta) / (2 * a)

        print('\nCalculando..')
        sleep(1.5)

        print(f'\nx1 = {x1:.1f}, x2 = {x2:.1f}')

    continuar = input('\nDeseja continuar <s/n>? ').lower().strip()[0]
    while continuar not in 'sn':
        print('\n[Erro] Digite uma resposta válida.')
        continuar = input('\nDeseja continuar <s/n>? ').lower().strip()[0]
    if continuar != 'S' and continuar != 's':
        print('\nEncerrando..')
        sleep(1)
        print('\n<<< Obrigado por usar meu programa, volte sempre =)')
        sleep(1)
        break

    