from flask import Flask, redirect, request, render_template, url_for, flash

app = Flask(__name__, template_folder="templates")
app.secret_key='john'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    errorMessage = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            errorMessage = "Invalid Credentials. Please Try Again"
        else:
            flash("You have Successfully Logged In")
            return redirect(url_for('index'))
    return render_template('login.html', errorMessage=errorMessage)


if __name__ == '__main__':
    app.run(debug=True)