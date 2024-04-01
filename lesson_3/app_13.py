from flask import Flask, render_template, request, session
from flask_wtf.csrf import CSRFProtect

from lesson_3.forms_3 import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = b'6dd6c948bedfb0b07713ff250f1719a2f37b8a0fdeaac2745ffac15dd7ef81e9'
csrf = CSRFProtect(app)


@app.route('/')
@app.route('/index/')
def index():
    return 'HOME PAGE'


@app.route('/data/')
def data():
    return 'your data'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        # OBRABOTKA DATA
        pass
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
