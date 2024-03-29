# Задание №6.
# Создать страницу, на которой будет форма для ввода имени и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка возраста и
# переход на страницу с результатом или на страницу с ошибкой в случае некорректного возраста.

from pathlib import PurePath, Path
from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/', methods=['GET', 'POST'])
def hello_form():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello, {name}'
    return render_template('hello_form.html')


@app.route('/upload/', methods=['GET', 'POST'])
def upload_file_page():
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


@app.route('/image/')
def image_page():
    return render_template('image_page.html')


@app.route('/authorization/', methods=['GET', 'POST'])
def authorization_page():
    if request.method == 'POST':
        if request.form.get('login') == 'admin' and request.form.get('password') == '678400':
            return render_template('index.html')
        else:
            return render_template('404.html')
    return render_template('authorization_form.html')


@app.route('/count/', methods=['GET', 'POST'])
def word_count_page():
    if request.method == 'POST':
        sentence = request.form.get('sentence')
        word_count = len(sentence.split())
        return f'В предложении "{sentence}" содержится {word_count} слов'
    return render_template('counter_form.html')


@app.route('/calculator/', methods=['GET', 'POST'])
def calculator_page():
    if request.method == 'POST':
        first_num = request.form.get('first_num')
        second_num = request.form.get('second_num')
        operation = request.form.get('operation')
        if operation == '+':
            result = int(first_num) + int(second_num)
        elif operation == '-':
            result = int(first_num) - int(second_num)
        elif operation == '*':
            result = int(first_num) * int(second_num)
        elif operation == '/':
            if second_num == 0:
                return f'На ноль делить нельзя'
            else:
                result = int(first_num) / int(second_num)
        else:
            return f'Введите корректную операцию'
        return str(result)
    return render_template('calculate_form.html')


@app.route('/age/', methods=['GET', 'POST'])
def age_form():
    if request.method == 'POST':
        age = int(request.form.get('age'))
        name = request.form.get('name')
        if age > 18:
            return render_template('index.html')
        else:
            return f'Пользователь {name} не достиг совершеннолетия. Вход запрещен'
    return render_template('age.html')


if __name__ == '__main__':
    app.run(debug=True)
