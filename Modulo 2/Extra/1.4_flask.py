# EXERCICIO 1.4: Rota com número (tipagem na rota)
# Crie uma rota '/dobro/<int:numero>' que recebe um número e retorna o dobro dele.

from flask import Flask

app = Flask(__name__) # representa o nome do arquivo
# o código deve ser escrito entre o app e o app.run

@app.route('/') # @decorador de função
def home():

    return 'Ola Mundo!'
@app.route('/sobre')
def sobre():
    return "Ola, meu nome e Alexsandra e sou uma desenvolvedora Python."

@app.route('/saudacao/<nome>') # para abrir a página precisamos adicionar o nome
def saudacao(nome) :
    return f'Ola {nome}! Tudo bem?'

@app.route('/dobro/<int:numero>') # uma rota não aceita '.', ou seja, não usamos float. Sem a informação do tipo de dado o python concatena
def dobro(numero): 
    return f'O dobro de {numero} e {2*numero}.'

if __name__ == '__main__':
    app.run(debug=True)
