import requests

# definir o nome para consulta
nome=input("Digite o nome da pessoa: ") . strip()

# url da api
url = f'https://api.agify.io/?name={nome}'

# Fazer a requisição
response = requests.get(url)

# Processar a resposta
if response. status_code == 200:
    dados = response. json()
    print(f"Nome:{dados['name']}")
    print(f"Idade estimada: {dados['age']} anos")
    print(f"Numero de registros anlisando: {dados['count' ]}")
else:
    print(f'Erro ao acessar a API: {response. status_code}')