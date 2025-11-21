# Exercício 2.2: Links entre rotas
# Adicione um menu de navegação simples com links
# para todas as suas rotas(/,/sobre,/saudacao,etc.).
# Passar a varivél através do url_for dentro do script
# html: ("{{url_for('saudacaa', nome='Joao' ) } }")
#'saudacao' é o nome da funcao Python que define a rota.
# nome='João' está passando o valor para a variável que a rota espera (<nome>)

from flask import Flask, render_template

app= Flask(__name__)# instanciando o flask

@app. route('/')
def index():
    return render_template('ex_2-2.html')

@app.route('/sobre')
def sobre():
    return 'Olá, eu sou aluno do projeto Fábrica de Programadores.'

@app.route('/saudacao/<nome>') # para abrir a página precisamos adicionar o nome
def saudacao(nome) :
    return f'Ola {nome}! Tudo bem?'

@app.route('/dobro/<int:numero>') # uma rota não aceita '.', ou seja, não usamos float. Sem a informação do tipo de dado o python concatena
def dobro(numero): 
    return f'O dobro de {numero} e {2*numero}.'

if __name__ == '__main__':
    app.run(debug=True)
