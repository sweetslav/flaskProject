# Задание №4.
# Написать функцию, которая будет принимать на вход строку и выводить на экран ее длину.

# Задание №3.
# Написать функцию, которая будет принимать на вход два числа и выводить на экран их сумму.

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


# @app.route('/about/')
# def about():
#     return 'Страница с описанием сайта'
#
#
# @app.route('/contact/')
# def contact():
#     return 'Страница для обратной связи'
#
#
# @app.route('/<int:a>/<int:b>/')
# def summa(a, b):
#     return str(a + b)


@app.route('/<string:text>/')
def str_length(text):
    return str(len(text))


if __name__ == '__main__':
    app.run(debug=True)
