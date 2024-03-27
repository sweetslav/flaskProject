from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Home page'


@app.route('/submit/', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello {name}!'
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
