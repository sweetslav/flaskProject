from flask import Flask, render_template, request, abort
#from lesson_2.db import get_blog

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Home page</h1>'


@app.route('/blog/<int:post_id>')
def get_blog_by_id(post_id):
    result = get_blog(post_id)
    if result is None:
        abort(404)


@app.errorhandler(404)
def page_not_found(e):
    app.logger.warning(e)
    context = {
        'title': 'Нет такой страницы :(',
        'url': request.base_url
    }
    return render_template('404.html', **context), 404


@app.errorhandler(500)
def page_internal_error(e):
    app.logger.error(e)
    context = {
        'title': 'Ошибка сервера :(',
        'url': request.base_url
    }
    return render_template('500.html', **context), 500


if __name__ == '__main__':
    app.run(debug=True)
