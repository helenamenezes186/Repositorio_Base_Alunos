# Ler o arquivo e exibir o texto em letras maiúsculas

with open('mensagem.txt','r') as arquivo:
    for linha in arquivo: # aqui percorremos as linhas do arquivo
        print(linha.strip() .upper()) # imprimimos cada linha em letra maiúscula e
# tiramos os espaços