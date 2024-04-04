# Задание №2.
# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания, количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
# Написать функцию-обработчик, которая будет выводить список всех книг с указанием их авторов.

from flask import Flask, render_template
from faker import Faker
from seminar_3.models_2 import db, Book, Author
from sqlalchemy.exc import IntegrityError
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task2books.db'
db.init_app(app)

fake = Faker()


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/books/')
def get_books():
    books = Book.query.all()
    context = {'books': books}
    return render_template('books.html', **context)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('DB Initialized')


@app.cli.command('fill-db')
def fill_db():
    count = 15
    for _ in range(count):
        new_author = Author(name=fake.first_name(),
                            last_name=fake.last_name())
        db.session.add(new_author)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()

    authors = Author.query.all()

    for _ in range(count):
        author = random.choice(authors)
        new_book = Book(title=fake.text(max_nb_chars=50),
                        year=fake.random_int(min=1900, max=2024),
                        number_of_copies=fake.random_int(min=1, max=5),
                        author_id=author.id)
        db.session.add(new_book)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()

    print('Данные успешно добавлены.')


@app.cli.command('clear-db')
def clear_db():
    Book.query.delete()
    Author.query.delete()
    db.session.commit()
    print('База данных успешно очищена.')


if __name__ == '__main__':
    app.run(debug=True)
