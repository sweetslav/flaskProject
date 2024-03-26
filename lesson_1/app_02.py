from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, guest!"


@app.route('/Святослав/')
def nike():
    return 'Привет, Святослав!'


@app.route('/Иван/')
def ivan():
    return 'Привет, Иван!'


if __name__ == '__main__':
    app.run(debug=True)
