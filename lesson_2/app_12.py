from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = b'a68a4fb7964607e898f09ab93780284e51b0532b06cf9dcc6ed57c5786d96f9d'


@app.route('/')
def index():
    return '<h1>Добро пожаловать на главную страницу</h1>'


@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        flash('Форма успешно отправлена', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run(debug=True)
