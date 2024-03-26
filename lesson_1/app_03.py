from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hi!"


@app.route('/Святослав/')
@app.route('/Свят/')
@app.route('/Svyat/')
def svyat():
    return 'Привет, Свят)'


if __name__ == '__main__':
    app.run(debug=True)
