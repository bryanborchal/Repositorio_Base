from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('ex_2-1.html')

@app.route('/sobre')
def sobre():
    return 'Fábrica de fazer programa!'


if __name__ == '__main__':
    app.run(debug=True)
