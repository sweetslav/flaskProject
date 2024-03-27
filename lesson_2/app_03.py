from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Home page'


@app.route('/about/')
def about():
    context = {
        'title': 'Обо мне',
        'name': 'Святослав'
    }
    return render_template('about.html', **context)


if __name__ == '__main__':
    app.run(debug=True)