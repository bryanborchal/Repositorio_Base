from flask import Flask #(flask = biblioteca, Flask = )

app = Flask(__name__) #cria uma instancia de Flask

@app.route('/')
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)