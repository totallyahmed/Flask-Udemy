#URL BINDING
from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/Joe')
def hello_Joe():
    return 'Hello Joe'

@app.route('/John/<John>')
def hello_John(John):
    return 'Hello %s as John' %John

@app.route('/user/<name>')
def hello_user(name):
    if name == 'Joe':
        return redirect(url_for('hello_Joe'))
    else:
        return redirect(url_for('hello_John'))

if __name__ == '__main__':
    app.run(debug=True)