from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Добро пожаловать на главную страницу</h1>'


@app.route('/redirect')
def redirect_to_index():
    return redirect(url_for('index'))


@app.route('/external/')
def external_redirect():
    return redirect('https://www.python.org/')


@app.route('/hello/<name>')
def hello(name):
    return f'Hello {name}!'


@app.route('/redirect/<name>')
def redirect_to_hello(name):
    return redirect(url_for('hello', name=name))


if __name__ == '__main__':
    app.run(debug=True)
