from flask import Flask, request, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "john"

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + "<b><a href = '/logout'> Click here to logout</a></b>"
    return "You are not logged in <br><a href = '/login'></b>" + "Click here to Login </b></a>"


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method=='POST' and request.form['username']=='ahmed':
        session['username'] = request.form['username']
        return redirect(url_for('success'))
    return '''
    <form action="" method="POST">
        <p><input type="text" name="username"></p>
        <p><input type="submit" value="Login"></p>
    </form>

    '''

@app.route('/success')
def success():
    return "Login Success"


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)