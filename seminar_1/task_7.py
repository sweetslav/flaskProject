# Задание №7.
# Написать функцию, которая будет выводить на экран HTML страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости, краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через контекст.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    return f'You are in the main page!'


@app.route('/news/')
def news():
    context = [
        {
            'title': 'Заголовок новости 1',
            'description': 'Краткое описание новости 1.',
            'date': '2024-03-26'
        },
        {
            'title': 'Заголовок новости 2',
            'description': 'Краткое описание новости 2.',
            'date': '2024-03-25'
        },
        {
            'title': 'Заголовок новости 3',
            'description': 'Краткое описание новости 3.',
            'date': '2024-03-24'
        }
    ]
    return render_template('news.html', context=context)


if __name__ == '__main__':
    app.run(debug=True)
