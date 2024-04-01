from flask import Flask
from lesson_3.models_02 import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Home page'


if __name__ == '__main__':
    app.run(debug=True)
