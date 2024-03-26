# Задание №2.
# Дорабатываем задачу 1.
# Добавьте две дополнительные страницы в ваше веб приложение:
# ○ страницу "about"
# ○ страницу "contact".

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/about/')
def about():
    return 'My name is Svyatoslav'


@app.route('/contact/')
def contact():
    return 'My phone number is 8 800 555 35 35'


if __name__ == '__main__':
    app.run(debug=True)
