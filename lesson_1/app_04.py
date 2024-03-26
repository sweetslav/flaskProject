from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/<name>/')
def hello(name='unknown'):
    return f'Hello, {name.capitalize()}!'


@app.route('/file/<path:file>/')
def set_path(file):
    print(type(file))
    return f'Path to file "{file}"'


@app.route('/number/<float:num>/')
def set_number(num):
    print(type(num))
    return f'Given number is {num}'


if __name__ == '__main__':
    app.run(debug=True)
