from flask import Flask, render_template
app = Flask(__name__)


# $env:FLASK_ENV= 'development'; $env:FLASK_APP='hello.py'; flask run
# $env:FLASK_APP='hello.py'; flask run
# FLASK_APP=hello.py flask run


@app.route('/')
def hello_world():
    name = 'Jared'
    return render_template('index.html', name=name)


@app.route('/crazy')
def crazy_world():
    return 'Crazy!!!!!WORLD!'


@app.route('/name/<name>')
def name_me(name):
    return f'Hello, {name}'
