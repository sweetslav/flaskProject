from flask import Flask
from lesson_3.models_05 import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hello World!'


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')


@app.cli.command('add-john')
def add_user():
    user = User(username='John', email='john@example.com')
    db.session.add(user)
    db.session.commit()
    print('John was added successfully')


@app.cli.command('edit-john')
def edit_user():
    user = User.query.filter_by(username='John').first()
    user.email = 'new_email@example.com'
    db.session.commit()
    print('Edit John mail was successful')


@app.cli.command('del-john')
def del_user():
    user = User.query.filter_by(username='John').first()
    db.session.delete(user)
    db.session.commit()
    print('John was deleted successfully')


if __name__ == '__main__':
    app.run(debug=True)
