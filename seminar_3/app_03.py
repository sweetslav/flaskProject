# Задание №3.
# Доработаем задача про студентов.
# Создать базу данных для хранения информации о студентах и их оценках в учебном заведении.
# База данных должна содержать две таблицы: "Студенты" и "Оценки".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа и email.
# В таблице "Оценки" должны быть следующие поля: id, id студента, название предмета и оценка.
# Необходимо создать связь между таблицами "Студенты" и "Оценки".
# Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их оценок.

from flask import Flask, render_template
from faker import Faker
from seminar_3.models import db, Book, Author, Student, Faculty, Grade
from sqlalchemy.exc import IntegrityError
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task3.db'
db.init_app(app)

fake = Faker()


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/students/')
def get_students():
    students = Student.query.all()
    context = {'students': students}
    return render_template('students.html', **context)


@app.route('/books/')
def get_books():
    books = Book.query.all()
    context = {'books': books}
    return render_template('books.html', **context)


@app.route('/faculties/')
def get_faculties():
    faculties = Faculty.query.all()
    context = {'faculties': faculties}
    return render_template('faculties.html', **context)


@app.route('/authors/')
def get_authors():
    authors = Author.query.all()
    context = {'authors': authors}
    return render_template('authors.html', **context)


@app.route('/grades/')
def get_grades():
    grades = Grade.query.all()
    context = {'grades': grades}
    return render_template('grades.html', **context)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('База данных успешно инициализирована.')


@app.cli.command('fill-authors')
def fill_authors():
    count = 15
    for _ in range(count):
        new_author = Author(name=fake.first_name(),
                            last_name=fake.last_name())
        db.session.add(new_author)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
    print('Авторы успешно добавлены.')


@app.cli.command('fill-books')
def fill_books():
    count = 20
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
    print('Книги успешно добавлены.')


@app.cli.command('fill-faculty')
def fill_faculty():
    faculties = ['Факультет 1', 'Факультет 2', 'Факультет 3']
    for faculty_name in faculties:
        new_faculty = Faculty(name=faculty_name)
        db.session.add(new_faculty)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
    print('Факультеты успешно добавлены.')


@app.cli.command('fill-students')
def fill_students():
    faculties = Faculty.query.all()  # Получаем список всех факультетов
    count = 20
    for faculty in faculties:
        for _ in range(count):
            new_student = Student(
                name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                age=fake.random_int(min=18, max=30),
                gender=fake.random_element(elements=("male", "female")),
                group=fake.random_int(min=100, max=999),
                faculty_id=faculty.id
            )
            db.session.add(new_student)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()

    print('Студенты успешно добавлены.')


@app.cli.command('fill-grades')
def fill_grades():
    students = Student.query.all()  # Получаем список всех студентов
    subjects = ['Математика', 'Физика', 'Химия', 'Биология', 'История']  # Список предметов
    grade_list = ['Плохо', 'Удовлетворительно', 'Хорошо', 'Отлично']  # Список оценок

    for student in students:
        for subject in subjects:
            # Проверяем, есть ли уже оценка для данного студента и предмета
            existing_grade = Grade.query.filter_by(student_id=student.id, subject=subject).first()
            if not existing_grade:
                # Если оценки нет, создаем новую
                new_grade = Grade(
                    student_id=student.id,
                    grade=fake.random_element(elements=grade_list),
                    subject=subject
                )
                db.session.add(new_grade)

    try:
        db.session.commit()
        print('Оценки успешно добавлены.')
    except IntegrityError:
        db.session.rollback()
        print('Ошибка при добавлении оценок.')


@app.cli.command('clear-db')
def clear_db():
    Book.query.delete()
    Author.query.delete()
    Faculty.query.delete()
    Student.query.delete()
    Grade.query.delete()
    db.session.commit()
    print('База данных успешно очищена.')


if __name__ == '__main__':
    app.run(debug=True)
