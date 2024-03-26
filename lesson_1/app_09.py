from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'main page'


@app.route('/for/')
def show_for():
    context = {
        'title': 'Цикл',
        'poem': ['Вот не думал не гадал,',
                 'Программистом взял и стал.',
                 'Хитрый знает он язык,',
                 'Он к другому не привык',
                 ]}
    return render_template('show_for.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
