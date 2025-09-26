#Criar um arquivo nomes.txt

nomes = ['Joao\n' , 'Maria\n' , 'Ana\n' ] # criamos uma lista com nomes para ser
# inseridos no arquivo nomes.txt

with open('nomes.txt', 'w', encoding='utf-8') as arquivo: # estamos
#criando o arquivo
    arquivo.writelines(nomes) # estamos pendido para escrever