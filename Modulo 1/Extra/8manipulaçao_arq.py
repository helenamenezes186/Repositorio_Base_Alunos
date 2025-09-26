# Contar quantas linhas tem no arquivo

with open('pessoa.txt','r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines() # aqui estamos lendo o arquivo e armazenando
    # a leitura na variável linhas
    print('Total linhas: ', len(linhas)) # a função len() conta quantas
    # linhas tem no arquivo lido