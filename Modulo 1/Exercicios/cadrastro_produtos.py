# Cadastro de produtos com relatório

# Crie um programa em Python que permita cadastrar produtos
# salver essas informações em um arquivo chamado produtos.txt
# O programa dever permitir:
# inserir o nome do produto e preço
# gravar os produtos no arquivo (um por linha)
# ler os dados do arquivo e gerar um relatório com:
# - lista de produtos cadastrados
# - média dos preços
# - o produto mais caro e o mais barato

#criar o arquivo produtos.txt e escrever os produtos
# Criar o arquivo produtos.txt e escrever os produtos
with open('produtos.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Cafe, 36.00\n')
    arquivo.write('Chá, 10.00\n')
    arquivo.write('Suco, 18.50\n')
    arquivo.write('Refrigerante, 17.50\n')
    arquivo.write('agua, 5.50\n')

#ler os produtos do arquivo
produtos =[]
with open('produtos.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        nome, preco = linha.strip().split(',')
        produtos. append(nome,float(preco))

total = 0
mais_caro = produtos[0]
mais_barato = produtos[0]

for nome, preco in produtos:
    total +=preco # percorre a lista produtos e soma cada preço encontrado
    if preco > mais_caro[1]:
        mais_caro = (nome, preco)

    if preco < mais_barato[1]:
        mais_barato = (nome, preco)

media= total/len(produtos)

# Criar o relatório
with open('relatorio_produtos.txt', 'w', encoding='utf-8') as relatorio:
    relatorio.write('Lista de Produtos\n')
    for nome, preco in produtos:
        relatorio.write(f'{nome}: R${preco :. 2f}\n')

        relatorio.write(f'\nPreco Médio: R$ {media :. 2f}\n')
        relatorio.write(f'Produto mais caro: {mais_caro[0]} R${mais_caro[1] :. 2f}\n')
        relatorio.write(f'Produto mais barato: {mais_barato[0]}R${mais_barato[1] :. 2f}\n')