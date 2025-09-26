# ler e imprimir o conteudo do arquivo mensagem.txt

with open('mensagem.txt', 'r', encoding='utf-8') as arquivo: 
    print(arquivo.read()) # aqui estamos imprmindo o que o arquivo leu na memoria 
    # e neste caso, não estamos armazenando em nehuma variavel 