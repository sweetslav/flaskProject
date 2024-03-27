from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Home page'


@app.get('/submit/')
def submit_get():
    return render_template('form.html')


@app.post('/submit/')
def submit_post():
    name = request.form.get('name')
    return f'Your name is {name}'


if __name__ == '__main__':
    app.run(debug=True)
