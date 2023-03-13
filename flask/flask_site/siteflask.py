from flask import Flask, render_template

app = Flask(__name__)

# criando pagina no flask
    # route -> casteloarcano.com.br
    # função -> o que vai ser exibido
    # template -> html que será mostrado

# Rotas
@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

@app.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return nome_usuario


# Roda o site
if __name__ == "__main__":
    app.run(debug=True)