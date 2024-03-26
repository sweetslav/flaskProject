from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'main page'


@app.route('/users/')
def users():
    _users = [{'name': 'Никанор',
               'mail': 'nik@mail.ru',
               'phone': '+7-987-654-32-10',
               },
              {'name': 'Феофан',
               'mail': 'feo@mail.ru',
               'phone': '+7-987-444-32-11',
               },
              {'name': 'Оверран',
               'mail': 'forrest@mail.ru',
               'phone': '+7-937-624-32-22',
               }, ]
    context = {
        'users': _users,
        'title': 'Точечная нотация'}
    return render_template('users.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
