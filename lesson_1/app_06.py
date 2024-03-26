from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/index/')
def html_index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
