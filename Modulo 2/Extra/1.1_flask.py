#EXERCICIO 1.1: Hello FLask!
# Crie um app Flask básico que exibe "Olá, mundo!" na rota principal (/).

from flask import Flask

app = Flask(__name__) # representa o nome do arquivo
# o código deve ser escrito entre o app e o app.run

@app.route('/') # @decorador de funçao
def home():

    return 'Olá Mundo!'

if __name__=='__main__':
    app.run(debug=True)
