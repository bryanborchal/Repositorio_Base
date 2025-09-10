from flask import Flask #(flask = biblioteca, Flask = )

app = Flask(__name__) #cria uma instancia de Flask

@app.route('/')
def index():
    return 'Hello World'


@app.route('/sobre')
def sobre():
    return 'Olá meu nome é Bryan, aprendiz de programação!'

if __name__ == '__main__':
    app.run(debug=True)