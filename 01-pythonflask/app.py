from flask import Flask, render_template, request # render_template, carregar o template
from models.logica import *

app = Flask(__name__) # acessando a biblioteca flask

@app.route('/') #  utilizando o metodo route
def home ():
    return render_template('index.html')

# para '/combustivel'
@app.route('/combustivel', methods = ['GET', 'POST']) # oque é GET e POST? fazer leitura no blog da profª
def combustivel():
    total = None
    mensagem = None

    if request.method == 'POST': # usando o POST na rota vai ser executado
        litros = float(request.form['litros'])
        preco = float(request.form['preco'])
        total, mensagem = calcular_combustivel(litros, preco) # disparar o calcula do que esta na logica.py 

    return render_template('combustivel.html', total=total, mensagem=mensagem)

# para '/joias'
@app.route('/joias', methods = ['GET', 'POST']) 
def joias(): # quando entrar na tela de joias, primeira tela aparece vazio
    resultado = None 

    if request.method == 'POST':
        valor = float(request.form['valor'])
        percentual = float(request.form['percentual'])
        resultado = calcular_joias(valor, percentual)

    return render_template('joias.html', resultado=resultado)

# para educacao
@app.route('/educacao', methods = ['GET', 'POST'])
def educacao():
    media = None
    status = None

    if request.method == 'POST':
        n1 = float(request.form['nota1'])
        n2 = float(request.form['nota2'])
        media, status = calcular_media(n1, n2)

    return render_template('educacao.html', media=media, status=status)

if __name__ == '__main__':
    app.run(debug=True)



