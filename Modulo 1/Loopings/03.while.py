letra= 's'
while letra== 's':
    n1=float(input('digite um numero: '))
    n2=float(input('digite a porcentagem que deseja descobrir: '))

    porcentagem=(n1*n2)/100
    print(f'a porcentagem é igual a : {porcentagem}')
    letra= input('deseja continuar? (s/n)').lower()