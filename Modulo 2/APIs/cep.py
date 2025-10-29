# Crie uma api que consulte o cep e informe o endereço

# Iniciamos fazendo a importação da biblioteca requests
import requests

# Indicamos a url para consulta da api
cep = input("Digite o CEP (somente números): ").strip() # usuario informa o cep que deseja consultar
url = f'https://viacep.com.br/ws/{cep}/json/' # endereco de url formatado para pesquisa do cep

# Fazemos a requisição
resposta = requests.get(url) # aqui estamos fazendo a requisição

if resposta.status_code == 200:
    dados = resposta.json()
    if 'erro' not in dados:
        print(f'CEP: {dados['cep']}')
        print(f'Logradouro: {dados['logradouro' ]}')
        print(f'Bairro: {dados['bairro']}')
        print(f'Cidade: {dados['localidade']}')
        print(f'Estado: {dados['uf']}')
    else:
        print('CEP nao foi encontrado')
else:
    print(f'Erro na requisicão: {resposta.status_code}')
    print(resposta.content)