# Задание №1.
# Создать страницу, на которой будет кнопка "Нажми меня".
# При нажатии на кнопку будет переход на другую страницу с приветствием пользователя по имени.

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)


@app.route('/')
def html_index():
    return render_template('index.html')


@app.get('/hello/')
def form_view_get():
    return render_template('hello_form.html')


@app.post('/submit/')
def submit():
    name = request.form.get('name')
    return f'Hello, {name}'


if __name__ == '__main__':
    app.run(debug=True)
