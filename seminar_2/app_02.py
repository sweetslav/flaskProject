# Задание №2.
# Создать страницу, на которой будет изображение и ссылка на другую страницу,
# на которой будет отображаться форма для загрузки изображений.

from pathlib import PurePath, Path
from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def html_index():
    return render_template('index.html')


@app.get('/hello/')
def html_form():
    return render_template('hello_form.html')


@app.post('/submit/')
def submit_form():
    name = request.form.get('name')
    return f'Hello, {name}'


@app.get('/upload/')
def html_upload_form():
    return render_template('upload_form.html')


@app.post('/upload/')
def upload():
    file = request.files.get('file')
    if file:
        file_name = secure_filename(file.filename)
        save_directory = Path.cwd() / 'uploads'
        save_directory.mkdir(parents=True, exist_ok=True)
        file.save(save_directory / file_name)
        save_path = PurePath.joinpath(Path.cwd(), 'uploads', file_name)
        print("Путь сохранения файла:", save_path)
        return f"Файл {file_name} загружен на сервер"


@app.get('/image_page/')
def html_image_page():
    return render_template('image_page.html')


if __name__ == '__main__':
    app.run(debug=True)
