#crie um programa que some todos os numeros imparea
#que são multiplos de 3 e 1 a 30 e apresente o resultado

#etapas para a resolução:
#1) criar um for de para captar os numeros impares
#2) criar uma condicional para checar se o numero é multiplo de 3
#3) somar os numeros que atende a condicional
#4) apresentar os resultados 

multiplo_tres=0 

for i in range(1,31,2):
    if i % 3==00:
        print (i, end=','):
        multiplo_tres+=i
print()
print(f'a soma dos numeros impares multiplos de 3 neste intervalo é {multiplo_tres}.')