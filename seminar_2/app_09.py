# Задание №9.
# Создать страницу, на которой будет форма для ввода имени и электронной почты
# При отправке которой будет создан cookie файл с данными пользователя
# Также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными пользователя и
# произведено перенаправление на страницу ввода имени и электронной почты.

from pathlib import PurePath, Path
from flask import Flask, render_template, request, url_for, flash, redirect, session, make_response
from werkzeug.utils import secure_filename

app = Flask(__name__)

# >>> imports secrets
# >>> secrets.token_hex()

app.secret_key = b'eefd12a8c23b37b1f64725b258b6169f2c461791e271c95bc553fdc25aad50bd'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/', methods=['GET', 'POST'])
def say_hello():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello, {name}'
    return render_template('hello_form.html')


@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
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
def html_image_page():
    return render_template('image_page.html')


@app.route('/authorization/', methods=['GET', 'POST'])
def authorization():
    if request.method == 'POST':
        if request.form.get('user_login') == 'admin' and request.form.get('user_password') == '678400':
            return render_template('index.html')
        else:
            return render_template('404.html')
    return render_template('authorization_form.html')


@app.route('/count/', methods=['GET', 'POST'])
def word_counter():
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


@app.route('/age/', methods=['GET', 'POST'])
def age_validation():
    if request.method == 'POST':
        age = int(request.form.get('age'))
        name = request.form.get('name')
        if age > 18:
            return render_template('index.html')
        else:
            return f'Пользователь {name} не достиг совершеннолетия. Вход запрещен'
    return render_template('age.html')


@app.route('/square/', methods=['GET', 'POST'])
def calculate_square_of_number():
    if request.method == 'POST':
        number = int(request.form.get('square_num'))
        return str(number * number)
    return render_template('square_page.html')


@app.route('/greeting/', methods=['GET', 'POST'])
def flash_greeting():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'Привет, {name}!', category='success')
        return redirect(url_for('flash_greeting', name=name))
    return render_template('greeting_page.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        email = request.form['user_email']
        response = make_response(redirect(url_for('welcome')))
        response.set_cookie('username', name)
        response.set_cookie('user_email', email)
        return response
    return render_template('login_form.html')


@app.route('/welcome/')
def welcome():
    username = request.cookies.get('username')
    if username:
        return render_template('welcome.html', username=username)
    else:
        return redirect(url_for('greeting'))


@app.route('/logout/')
def logout():
    response = make_response(redirect(url_for('login')))
    response.set_cookie('username', '', expires=0)
    response.set_cookie('user_email', '', expires=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)
