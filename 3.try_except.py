# crie uma função chamada calculadora que receba tres parametros:
# dois numeros e uma operação (+, -,*, /)
# a função deve retornar o resultado da operação, mas precisa
#tratar as seguintes exceções:
# divisão por zero (zeroDivisionError)
# tipo de dado invalido (ValueError)

def calculadora():
    try:
        n=input('digite um numero ou x para sair do sistema: ')
        if n.lower() == 'x':
            print('are breve')
            return
        n1=input('digite um numero ou x para sair do sistema: ')
        if n1.lower()== 'x':
            print ('ate breve.')
        operador= input ('informme um operador matematico (+,-,*,/) ou x para sair do sistema: ')
        if operador.lower()=='x':
            print(' até breve')
            return
        
        n= float (n)
        n1= float(n1)

        if operador == '+':
            resultado= n+n1
        elif operador=='_': 
            resultado= n-n1
        elif operador== '*':
            resultado= n*n1
        elif operador== '/':
            resultado=n/n1
            if n1==0:
                raise ZeroDivisionError ('nao é possivel dividir por zero.')
            resultado=n/n1
        else:
            print('voce não escolheu um operador ou escolheu um comando invalido')
        print(f' operação: {n} {operador} {n1}={resultado}')
    except ValueError:
        print('voice digitou um caracter invalid, digite somente numeros')
    except ZeroDivisionError as zero:
        print (zero)
calculadora()