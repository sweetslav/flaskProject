# Задание №5.
# Создать страницу, на которой будет форма для ввода двух чисел и выбор операции
# (сложение, вычитание, умножение или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление результата выбранной операции и переход на страницу с результатом.


from pathlib import PurePath, Path
from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello, {name}'
    return render_template('form.html')


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
def image_page():
    return render_template('image_page.html')


@app.route('/authorization/', methods=['GET', 'POST'])
def authorization():
    if request.method == 'POST':
        if request.form.get('login') == 'admin' and request.form.get('password') == '678400':
            return render_template('index.html')
        else:
            return render_template('404.html')
    return render_template('authorization_form.html')


@app.route('/count/', methods=['GET', 'POST'])
def count_page():
    if request.method == 'POST':
        sentence = request.form.get('sentence')
        word_count = len(sentence.split())
        return f'В предложении "{sentence}" содержится {word_count} слов'
    return render_template('counter_form.html')


@app.route('/calculator/', methods=['GET', 'POST'])
def calculator():
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


if __name__ == '__main__':
    app.run(debug=True)
