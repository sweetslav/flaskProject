from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World!"


@app.route('/if/')
def show_if():
    context = {'title': "Ветвление",
               'user': 'Крутой хакер',
               'number': 1,
               }
    return render_template('show_if.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
