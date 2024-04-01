from flask import Flask
from lesson_3.app_03 import db, User, Post, Comment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hello World!'


@app.cli.command('init-db')
def init_db():
    # показать ошибку с неверным wsgi.py
    db.create_all()
    print('OK')


if __name__ == '__main__':
    app.run(debug=True)
