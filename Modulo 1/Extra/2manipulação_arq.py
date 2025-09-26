# Ler um arquivo

arquivo = open('pessoa.txt', 'r') # a leitura está sendo feita na memória
conteudo = arquivo.read() # eu armazeno a leitura em uma variavel
print(conteudo) # peço para imprimir a leitura
arquivo.close() # sempre que utilizamos a função open() precisamos finalizar
# fechando o arquivo