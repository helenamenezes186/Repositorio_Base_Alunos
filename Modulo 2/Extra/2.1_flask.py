# Exercício 2.1: HTML básico na resposta
# Modifique sua rota principal para retornar um pequeno HTML com título,
#parágrafo e um link para outra rota
# Usar render_template para renderizar um arquivo.html
# Usar url_for() nas ancoras tags do script html

from flask import Flask, render_template
app = Flask (__name__)

@app. route('/')
def index():
    return render_template('ex_2-1.html')

@app. route('/sobre')
def sobre():
    return 'Fabrica de Programadores'

@app.route('/zezinho')
def zezinho():
    return 'Achou a rota'

if __name__ == '__main__':
    app.run(debug=True)

