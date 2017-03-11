from flask import Flask, render_template, redirect, abort
import werkzeug.exceptions as ex
from binascii import hexlify
from os import urandom

app = Flask(__name__, static_folder='browser/static', template_folder='browser/templates')
PORT = 80


class NotFound(ex.HTTPException):
    code = 404
    description = 'This is not the page you are looking for.'

abort.mapping[404] = NotFound


def run():
    flask_options = dict(port=PORT, host='0.0.0.0', debug=True)
    app.secret_key = hexlify(urandom(24))#hexlify(bytes('development_', encoding='latin-1'))
    app.run(**flask_options)


@app.route('/', methods=['GET'])
def root():
    return redirect('/index')


@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    return 'beating', 200


@app.errorhandler(404)
def void_or_nonexistent_term(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    run()
