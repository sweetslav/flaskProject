from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@hostname/db_name'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://username:password@hostname/db_name'
db = SQLAlchemy(app)


@app.route('/')
@app.route('/index/')
def index():
    return 'Home Page'


if __name__ == '__main__':
    app.run(debug=True)
