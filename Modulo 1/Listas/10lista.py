#Dada a lista original = [1, 2, 3, 4], use .copy() para criar uma nova lista
#chamada copia. Altere a copia (adicione o número 99) e mostre as duas listas
#para verificar que são independentes.

original= [1,2,3,4]
print(f'lista original: {original}')

copia= original.copy()
print(f'lista copia: {copia}')

copia.append(99)
print(f"lista copia apos o append: {copia}")