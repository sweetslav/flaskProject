# Задание №8.
# Создать базовый шаблон для всего сайта, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для каждой отдельной страницы.
# Например, создать страницу "О нас" и "Контакты", используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    return 'main page'


@app.route('/about/')
def html_about():
    return render_template('about.html')


@app.route('/contacts/')
def html_contacts():
    return render_template('contacts.html')


if __name__ == '__main__':
    app.run(debug=True)
