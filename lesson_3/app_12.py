from flask_wtf import CSRFProtect
from flask import Flask

app = Flask(__name__)
# import secrets
# secrets.token_hex()
app.config['SECRET_KEY'] = b'6dd6c948bedfb0b07713ff250f1719a2f37b8a0fdeaac2745ffac15dd7ef81e9'
csrf = CSRFProtect(app)

@app.route('/')
@app.route('/index/')
def index():
    return 'HOME PAGE'


@app.route('/form/', methods=['GET', 'POST'])
@csrf.exempt
def my_form():
    ...
    return 'No CSRF protected'


if __name__ == '__main__':
    app.run(debug=True)