from flask import Flask

app = Flask(__name__)

html = '''
<h1>Hello, my name is Svyatoslav</h1>
<p>I create sites on Flask.<br>Look at!</p>
'''


@app.route('/')
def index():
    return 'Hi!'


@app.route('/text/')
def text():
    return html


@app.route('/poems/')
def poems():
    poem = ['The quick brown fox jumps,',
            'the lazy dog',
            'the fox jumps over the lazy',
            ]
    txt = '<h1>Poem</h1>\n<p>' + '<br/>'.join(poem) + '</p>'
    return txt


if __name__ == '__main__':
    app.run(debug=True)
