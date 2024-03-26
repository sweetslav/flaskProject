from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'main page'


@app.route('/main/')
def main():
    context = {'title': 'Главная'}
    return render_template('new_main.html', **context)


@app.route('/data/')
def data():
    context = {'title': 'База статей'}
    return render_template('new_data.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
