# crie um codigo em python que peça um numero ao usuario
# e exiba "numero par" se ele for divisivel por 2

# etapas de ressolução

#1)solicitar um numero ao usuario
#2) verificar se onumero é par ou inpar
#3) informar se o numero é par ou inpar

numero= float(input("digite um numero:"))

if numero % 2 == 0:
    print(f"o numero {numero} é par. ")
else: print(f"o numero {numero} é inpar")