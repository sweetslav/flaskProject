# Задание №5.
# Написать функцию, которая будет выводить на экран HTML страницу с заголовком "Моя первая HTML страница"
# и абзацем "Привет, мир!".

from flask import Flask, render_template

app = Flask(__name__)
first = '''
<h1> Моя первая страница</h1>
<p>Привет мир</p>
'''


@app.route('/')
def hello():
    return first


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
#
#
# @app.route('/<string:text>/')
# def str_length(text):
#     return str(len(text))

if __name__ == '__main__':
    app.run(debug=True)
