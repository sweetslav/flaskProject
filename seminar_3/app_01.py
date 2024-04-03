# Задание №1.
# Создать базу данных для хранения информации о студентах университета.
# База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название факультета.
# Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их факультета.

from flask import Flask, render_template
from seminar_3.models import db, Student, Faculty
from sqlalchemy.exc import IntegrityError
from random import choice
from faker import Faker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase1.db'
db.init_app(app)
fake = Faker()


@app.route('/')
@app.route('/index/')
def index():
    return 'Homepage'


@app.route('/students/')
def get_students():
    students = Student.query.all()
    context = {'students': students}
    return render_template('students.html', **context)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')


@app.cli.command('fill-db')
def fill_tables():
    faculties = ['Факультет 1', 'Факультет 2', 'Факультет 3']
    for faculty_name in faculties:
        new_faculty = Faculty(name=faculty_name)
        db.session.add(new_faculty)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()

    for faculty_id in range(1, 4):
        for _ in range(1, 21):
            new_student = Student(
                name=fake.first_name(),
                last_name=fake.last_name(),
                age=fake.random_int(min=18, max=30),
                gender=fake.random_element(elements=("male", "female")),
                group=fake.random_int(min=100, max=999),
                faculty_id=faculty_id
            )
            db.session.add(new_student)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()


if __name__ == '__main__':
    app.run(debug=True)
