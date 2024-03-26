# Задание №6.
# Написать функцию, которая будет выводить на экран HTML страницу с таблицей, содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через контекст.


from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    students = [
        {
            'first_name': 'John',
            'last_name': 'Depp',
            'age': 29,
            'avg_score': 4.5

        },
        {
            'first_name': 'Bob',
            'last_name': 'Tompson',
            'age': 22,
            'avg_score': 4.1

        },
        {
            'first_name': 'Bill',
            'last_name': 'Pup',
            'age': 49,
            'avg_score': 2.5

        },
    ]
    context = {
        'person': students
    }
    return render_template('students.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
