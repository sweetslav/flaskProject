from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Home page</h1>'


@app.errorhandler(404)
def page_not_found(e):
    app.logger.warning(e)
    context = {
        'title': 'Нет такой страницы :(',
        'url': request.base_url
    }
    return render_template('404.html', **context), 404


if __name__ == '__main__':
    app.run(debug=True)
