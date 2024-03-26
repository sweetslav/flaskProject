# Задание №9.
# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы "Одежда", "Обувь" и "Куртка", используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def html_home_page():
    return render_template('base_shop.html')


@app.route('/clothes/')
def html_clothes_page():
    return render_template('clothes.html')


@app.route('/shoes/')
def html_shoes_page():
    return render_template('shoes.html')


@app.route('/accessories/')
def html_accessories_page():
    return render_template('accessories.html')


if __name__ == '__main__':
    app.run(debug=True)
