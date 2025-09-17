#crie um programa que leia o peso de 5 pessoas.
#no final, mostre qual foi o maior e o menor peso lido.

#etapas para resolução:
#1) crie uma lista vazia para receber os pesos
#2) crie um for para receber os pesos das 5 pessoas.
#4) utilize a função max() e min)() ou ordene a lsita e busque o primeiro e o ultimo elemento
#5) apresente os resultados

pesos=[]

for i in range(5):
    peso=float(input(f'digite o peso {i+1} (kg): '))
    pesos.append(peso)
print(f"a lista dos pesos em kg: ")
