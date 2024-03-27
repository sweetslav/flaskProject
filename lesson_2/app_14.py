from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/')
def index():
    # Устанавливаем cookie
    response = make_response('Cookie установлен')
    response.set_cookie('username', 'admin')
    return response


@app.route('/getcookie/')
def get_cookies():
    # Получаем значение cookie
    name = request.cookies.get('username')
    return f'Значение cookie: {name}'


if __name__ == '__main__':
    app.run(debug=True)
