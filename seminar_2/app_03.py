# Задание №3.
# Создать страницу, на которой будет форма для ввода логина и пароля
# При нажатии на кнопку "Отправить" будет произведена проверка соответствия логина и пароля
# и переход на страницу приветствия пользователя или страницу с ошибкой.

from pathlib import PurePath, Path
from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello, {name}'
    return render_template('hello_form.html')


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            file_name = secure_filename(file.filename)
            save_directory = Path.cwd() / 'uploads'
            save_directory.mkdir(parents=True, exist_ok=True)
            file.save(save_directory / file_name)
            save_path = PurePath.joinpath(Path.cwd(), 'uploads', file_name)
            print("Путь сохранения файла:", save_path)
            return f"Файл {file_name} загружен на сервер"
    return render_template('upload_form.html')


@app.route('/image_page/')
def html_image_page():
    return render_template('image_page.html')


@app.route('/authorization/', methods=['GET', 'POST'])
def authorization():
    if request.method == 'POST':
        if request.form.get('login') == 'admin' and request.form.get('password') == '678400':
            return render_template('index.html')
        else:
            return render_template('404.html')
    return render_template('authorization_form.html')


if __name__ == '__main__':
    app.run(debug=True)
